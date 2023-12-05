from phuocsiu.config.configuration import ConfigManager
from phuocsiu.components.ingest_data import DataIngestion
from phuocsiu.components.train import Training

inges_congfig = ConfigManager()
data_ingest = DataIngestion(config=inges_congfig.get_data_ingestion_config())
data_ingest.download_file()
data_ingest.extract_zip_file()

data_config ,model_config =  inges_congfig.get_data_config(),inges_congfig.get_model_config()
traner = Training(data_config,model_config)
traner.train()