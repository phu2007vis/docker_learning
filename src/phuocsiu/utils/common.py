import os
from box.exceptions import BoxValueError
import yaml
from phuocsiu import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def split_train_test_csv(csv_path : Path,save_dir) :

    if save_dir:
        pass
    else:
        pass
    

@ensure_annotations
def preprocessing(df :  pd.DataFrame,split_precent :float = 0.2) :

    df_clean_na =df.dropna()
    x,y = df_clean_na.iloc[:,0:-1].values,df_clean_na.iloc[:,-1].values
    x_min = x.min(axis=0)
    x_max = x.max(axis=0)
    x = (x-x_min)/(x_max-x_min)

    if split_precent == 0:
        return x,None,y,None
    x_train,x_test,y_train, y_test = train_test_split(x,y,test_size=split_precent)
    
    return x_train,x_test,y_train,y_test


@ensure_annotations
def preprocessing2(path: Path,split_precent :float = 0.0,sep = ";") :

    df = pd.read_csv(path,sep = sep)
    df_clean_na =df.dropna()
    x,y = df_clean_na.iloc[:,0:-1].values,df_clean_na.iloc[:,-1].values
    x_min = x.min(axis=0)
    x_max = x.max(axis=0)
    x = (x-x_min)/(x_max-x_min)

    if split_precent == 0:
        return x,None,y,None
    x_train,x_test,y_train, y_test = train_test_split(x,y,test_size=split_precent)
    
    return x_train,x_test,y_train,y_test

