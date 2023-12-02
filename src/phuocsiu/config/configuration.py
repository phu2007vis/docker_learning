from phuocsiu.constants import *
import os
from phuocsiu.entity.config_entity import DataIngestionConfig
from phuocsiu.utils.common import create_directories,read_yaml


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
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

