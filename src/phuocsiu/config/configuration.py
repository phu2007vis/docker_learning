from phuocsiu.constants import *
import os
from phuocsiu.entity.config_entity import *
from phuocsiu.utils.common import create_directories,read_yaml
from sklearn.ensemble import RandomForestClassifier

class ConfigManager:
    def __init__(
            self,
            config_filepath = CONFIG_PATH,
            params_filepath = PARAMS_PATH
            ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            data_dir_name = config.data_dir_name
        )

        return data_ingestion_config
    def get_data_config(self) -> DataConfig:
        config = self.config.train_config
        data_config = DataConfig(
            train_data= config.train_data,
            test_data = config.test_data,
            valid_pecent=config.valid_pecent,
            sep = config.sep
        )
        return data_config
    
    def get_model_config(self) -> ModelConfig:
        
        config = self.config.model_config

        return ModelConfig(
            n_estimators=self.params.n_estimators,
            model =  RandomForestClassifier(n_estimators=config.n_estimators),
            model_save= Path(config.model_save)
        )

    def get_mlflow_config(self) -> MflowConfig:
        
        config = self.config.mlflow
        return MflowConfig(
            MLFLOW_TRACKING_PASSWORD= config.MLFLOW_TRACKING_PASSWORD,
            MLFLOW_TRACKING_URI= config.MLFLOW_TRACKING_URI,
            MLFLOW_TRACKING_USERNAME= config.MLFLOW_TRACKING_USERNAME
        )