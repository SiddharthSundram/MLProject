import logging
import os
from datetime import datetime

# Just the file name (no 'logs/' here)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Folder path for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Create logs directory if it doesn't exist

# Full path to log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO
)
