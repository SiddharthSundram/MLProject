import os
import sys
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")


def read_sql_data():
    logging.info("Connecting to the database and reading data")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("Database connection established successfully",mydb)
        df = pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())
        return df
    
    except Exception as e:
        logging.error(f"Error occurred while reading SQL data: {e}")
        raise CustomException(e, sys) from e
