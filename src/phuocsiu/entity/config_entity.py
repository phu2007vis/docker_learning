from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL: str
    data_dir_name: str
    
@dataclass(frozen=True)
class TrainingConfig:
    data_file: str
    valid_pecent: float
@dataclass
class ModelConfig:
    n_estimators: int
    






