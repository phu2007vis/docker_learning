from phuocsiu.entity.config_entity import *
from phuocsiu.config.configuration import *
import pandas as pd
from phuocsiu.utils.common import preprocessing
import pickle
from phuocsiu import logger

class Training:
    def __init__(self, train_config: DataConfig,model_config: ModelConfig):
        self.train_config = train_config
        self.model_config = model_config
        self.df = pd.read_csv(self.train_config.train_data,sep = self.train_config.sep)

    def train(self):
        try:
            logger.info("------------------")
            logger.info("model training")
            train_x,_,train_y,_ = preprocessing(self.df,0.0)
            model = self.model_config.model.fit(train_x,train_y)
            path_save = self.model_config.model_save
            os.makedirs(path_save.parent,exist_ok = True)
            with open(path_save,"wb") as f:
                pickle.dump(model,f)
            logger.info(f"model training oke!, save at{path_save}")
            logger.info("------------------")
        except Exception as  e:
            logger.error("traning issue")
            raise e
        

        