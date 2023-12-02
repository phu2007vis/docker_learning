import os
import zipfile
import gdown
from phuocsiu import logger
from phuocsiu.utils.common import get_size
from phuocsiu.entity.config_entity import (DataIngestionConfig)



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = os.path.join(self.config.root_dir,self.config.data_dir_name+".zip")

            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = os.path.join(self.config.root_dir,self.config.data_dir_name)
        zip_file_path =os.path.join(self.config.root_dir,self.config.data_dir_name+".zip")
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)
