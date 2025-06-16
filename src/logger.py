
import logging
import os
import sys
import time

from src.connection import execute_command  # Assuming this is valid

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Get date-based filename
time_mod = time.strftime("%Y-%m-%d")

# Create logs directory
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
os.makedirs(log_path, exist_ok=True)

# Build full path to log file
log_file = os.path.join(log_path, f"{time_mod}.log")

# Configure logging
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Add console handler
console_handle = logging.StreamHandler()
console_handle.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handle.setFormatter(formatter)
logging.getLogger('').addHandler(console_handle)

# Test log
logger.info("Logging is now set up.")

def get_log_path():
    return log_path
