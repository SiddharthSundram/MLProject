from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("Starting the application...")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom exception occurred")
        raise CustomException(e, sys)
