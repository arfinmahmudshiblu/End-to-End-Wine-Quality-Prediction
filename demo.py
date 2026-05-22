# from wine_quality_prediction.logger import logging

# logging.info("Logging setup complete.")

# from wine_quality_prediction.logger import logging
# from wine_quality_prediction.exception import WineQualityPredictionException   
# import sys

# try:
#     r=3/0
# except Exception as e:
#     logging.info(e)
#     raise WineQualityPredictionException(e, sys) 

# import os

# mongodburl=os.getenv("MONGODB_URL")
# print(mongodburl)

from wine_quality_prediction.pipline.training_pipeline import TrainingPipeline


pipeline = TrainingPipeline()
pipeline.run_pipeline()


