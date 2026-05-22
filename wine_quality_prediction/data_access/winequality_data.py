from wine_quality_prediction.configuration.mongo_db_connection import MongoDBClient
from wine_quality_prediction.constants import DATABASE_NAME
from wine_quality_prediction.exception import WineQualityPredictionException
import pandas as pd
import sys
from typing import Optional
import numpy as np



class WineQualityPredictionData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise WineQualityPredictionException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop("_id", axis=1, inplace=True)
            df.replace("na", np.nan, inplace=True)
            return df
        except Exception as e:
            raise WineQualityPredictionException(e,sys)