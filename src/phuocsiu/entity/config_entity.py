from dataclasses import dataclass
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL: str
    data_dir_name: str
    
@dataclass(frozen=True)
class DataConfig:
    train_data: str
    test_data: str
    valid_pecent: float
    sep: str


@dataclass(frozen=True)
class ModelConfig:
    model : RandomForestClassifier
    n_estimators: int
    model_save: Path
    

    


@dataclass(frozen=True)
class MflowConfig:
    MLFLOW_TRACKING_URI: str
    MLFLOW_TRACKING_USERNAME: str
    MLFLOW_TRACKING_PASSWORD: str  


