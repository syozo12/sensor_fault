import os
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler,FunctionTransformer
from sklearn.pipeline  import Pipeline

from dataclasses import dataclass
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils

@dataclass
class DataTransformationConfig:
    artifact_dir=os.path.join(artifact_folder)
    transformed_train_file_path = os.path.join(artifact_dir,"train.npy")
    transformed_test_file_path = os.path.join(artifact_dir,"test.npy")
    transformed_object_file_path = os.path.join(artifact_dir,"preprocessing.pkl")


class DataTransformation:
    def __init__(self,feature_store_file_path):
        self.feature_store_file_path=feature_store_file_path
        self.data_transformation_config = DataTransformationConfig()
        self.utils = MainUtils()

    @staticmethod
    def get_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            logging.info(f"Data loaded successfully from {file_path}")
            return df
        except Exception as e:
            raise CustomException(e, sys)

    def get_data_transformation(self, data):
        try:
            logging.info("Starting data transformation")
            scaler = self.data_transformation_config.scaler
            transformed_data = scaler.fit_transform(data)
            logging.info("Data transformation completed")
            return transformed_data
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, raw_file_path):
        try:
            logging.info("Initiating data transformation process")
            os.makedirs(self.data_transformation_config.transformed_data_folder, exist_ok=True)
            data = self.get_data(raw_file_path)
            transformed_data = self.get_data_transformation(data)
            transformed_data_file_path = os.path.join(
                self.data_transformation_config.transformed_data_folder, "transformed_data.csv")
            pd.DataFrame(transformed_data).to_csv(transformed_data_file_path, index=False, header=True)
            logging.info(f"Transformed data saved at {transformed_data_file_path}")
            return transformed_data_file_path
        except Exception as e:
            raise CustomException(e, sys)
