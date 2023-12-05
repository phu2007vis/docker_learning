from phuocsiu.config.configuration import ConfigManager
from phuocsiu.entity.config_entity import *
import mlflow
from mlflow.models import infer_signature
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from phuocsiu.utils.common import preprocessing2
import pickle


class Validate:
    def __init__(self,config_manager : ConfigManager) -> None:

        self.data_config = config_manager.get_data_config()
        self.mlflow_config = config_manager.get_mlflow_config()
        self.params = dict(config_manager.params)
        os.environ["MLFLOW_TRACKING_URI"] = mlflow_config.MLFLOW_TRACKING_URI
        os.environ["MLFLOW_TRACKING_USERNAME"] = mlflow_config.MLFLOW_TRACKING_USERNAME
        os.environ["MLFLOW_TRACKING_PASSWORD"] = mlflow_config.MLFLOW_TRACKING_PASSWORD
        self.x_test,_, self.y_test ,_= preprocessing2(Path(self.data_config.test_data),0.0)
        path_model = config_manager.get_model_config().model_save
        self.model = pickle.load(open(path_model,"rb"))

   
      
    def validate(self):
        mlflow.end_run() 
        with mlflow.start_run():
            signature = infer_signature(self.x_test, self.model.predict(self.x_test))
            mlflow.log_params(self.params)
            mlflow.sklearn.log_model(
                sk_model=self.model,
                artifact_path="iris_model",
                signature=signature,
                input_example=self.x_test,
                registered_model_name="tracking-quickstart",
            )

