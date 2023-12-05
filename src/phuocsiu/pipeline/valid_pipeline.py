from phuocsiu.config.configuration import ConfigManager
from phuocsiu.entity.config_entity import *
import mlflow
from mlflow.models import infer_signature
import os
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
from phuocsiu.utils.common import preprocessing2
import pickle
from phuocsiu import logger


class Validate:
    def __init__(self,config_manager : ConfigManager) -> None:

        self.data_config = config_manager.get_data_config()
        self.mlflow_config = config_manager.get_mlflow_config()
        self.params = dict(config_manager.params)
        os.environ["MLFLOW_TRACKING_URI"] = self.mlflow_config.MLFLOW_TRACKING_URI
        os.environ["MLFLOW_TRACKING_USERNAME"] = self.mlflow_config.MLFLOW_TRACKING_USERNAME
        os.environ["MLFLOW_TRACKING_PASSWORD"] = self.mlflow_config.MLFLOW_TRACKING_PASSWORD
        self.x_test,_, self.y_test ,_= preprocessing2(Path(self.data_config.test_data),0.0)
        path_model = config_manager.get_model_config().model_save
        self.model = pickle.load(open(path_model,"rb"))

   
      
    def validate(self):
        mlflow.end_run() # End the active run
        functions= "accuracy_score,precision_score,recall_score,f1_score"
        functions= functions.split(sep=",")
        y_predict = self.model.predict(self.x_test)
     
        with mlflow.start_run():
            for name_funct in functions:
                try:
                    func = globals()[name_funct]
                    value = float(func(self.y_test, y_predict))
                except ValueError as e:
                    value = float(func(self.y_test, y_predict,average = "micro"))
                    # Handle the specific ValueError if needed
                except Exception as e:
                    raise e  # If you still want to raise the exception after handling   
                mlflow.log_metric(name_funct,value)
            signature = infer_signature(self.x_test, y_predict)
            mlflow.log_params(self.params)
            mlflow.sklearn.log_model(
                sk_model=self.model,
                artifact_path="iris_model",
                signature=signature,
                input_example=self.x_test,
                registered_model_name="MyFirstModel",
            )



if __name__ == "__main__":
    try:
        STAGE_NAME = "Start Valid"
        logger.info("----------")
        logger.info(STAGE_NAME)
        mger = ConfigManager()
        validator = Validate(mger)
        validator.validate()
        logger.info(f"{STAGE_NAME} succed")
    except Exception as e:
        logger.exception(e)
        raise e