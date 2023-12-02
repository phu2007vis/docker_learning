from phuocsiu.entity.config_entity import TrainingConfig
from phuocsiu.config.configuration import *
import pandas as pd
class Training:
    def __init__(self, train_config: TrainingConfig,model_config: ModelConfig):
        self.train_config = train_config
        self.model_config = model_config

        self.df = pd.read_csv("")
    def train()