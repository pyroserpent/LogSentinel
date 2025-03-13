import logging
import time
import random

# Define log file name
LOG_FILE_PATH = "logfile.log"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Sample log messages
log_messages = [
    ("INFO", "System running smoothly."),
    ("WARNING", "High memory usage detected."),
    ("ERROR", "Database connection failed."),
    ("CRITICAL", "System overheating! Immediate attention required."),
    ("INFO", "User logged in successfully."),
    ("ERROR", "File not found: config.yaml."),
    ("WARNING", "Disk space running low."),
    ("INFO", "Scheduled maintenance will start at midnight."),
    ("CRITICAL", "Unauthorized access attempt detected!"),
    ("ERROR", "Application crashed due to unknown error."),
]

# Function to generate logs dynamically
def generate_logs(n=20, delay=2):
    """Generate 'n' random log messages with a delay between each log entry."""
    for _ in range(n):
        level, message = random.choice(log_messages)
        if level == "INFO":
            logging.info(message)
        elif level == "WARNING":
            logging.warning(message)
        elif level == "ERROR":
            logging.error(message)
        elif level == "CRITICAL":
            logging.critical(message)

        print(f"Logged: {level} - {message}")  # Print to console
        time.sleep(delay)  # Simulate real-time logging delay

# Generate 20 log messages with a 2-second interval
generate_logs(n=20, delay=2)

print(f"✅ Log file '{LOG_FILE_PATH}' generated successfully.")
