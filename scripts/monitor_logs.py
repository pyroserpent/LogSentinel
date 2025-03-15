import re  # Regular expressions for pattern matching
import time # Time module for sleep intervals
import os # For file and directory operations
from watchdog.observers import Observer # For monitoring file system events
from watchdog.events import FileSystemEventHandler # For handling file system events

# Define the paths for the log files
LOG_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "logfile.log"))
ALERTS_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "alerts.log"))

class LogFileHandler(FileSystemEventHandler):
    """Handles log file changes and logs alerts to a file instead of sending real emails."""
    
    def __init__(self, file_path, alert_file):  # Initialize with the log file path and alert file path
        self.file_path = file_path  # Path to the log file
        self.alert_file = alert_file # Path to the alert log file
        self.last_position = 0  # Track last read position

    def on_modified(self, event): 
        """Triggered when the log file is modified."""
        if os.path.abspath(event.src_path) == self.file_path: # Check if the modified file is the log file
            with open(self.file_path, 'r') as f:
                f.seek(self.last_position)  # Move to last read position
                new_lines = f.readlines() # Read new lines from the log file
                self.last_position = f.tell()  # Update position
                # Check for error patterns in new lines
                for line in new_lines:
                    if re.search(r'ERROR|CRITICAL|FAILURE', line): # Look for error patterns
                        alert_message = f"🚨 EMAIL ALERT: {line.strip()}\n" # Format alert message
                        print(alert_message)  # Print to console
                        self.log_alert(alert_message)  # Log to file

    def log_alert(self, message):
        """Log the alert message to alerts.log."""
        with open(self.alert_file, "a", encoding="utf-8") as f:
            f.write(message) # Write the alert message to the alert log file (appends)

# Main execution that starts monitoring the log file
if __name__ == "__main__":
    if not os.path.exists(LOG_FILE_PATH): # Check if the log file exists
        print(f"⚠️ Log file '{LOG_FILE_PATH}' not found. Run 'generate_log.py' first.")
        exit(1) # Exit if the log file does not exist

    print(f"🔍 Monitoring {LOG_FILE_PATH} for errors...")

    event_handler = LogFileHandler(LOG_FILE_PATH, ALERTS_FILE_PATH) # Create an instance of the log file handler
    observer = Observer() # Create an observer to monitor file system events
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH), recursive=False) # Schedule the handler for the directory containing the log file

    observer.start() # Start the observer (monitoring)
    try:
        while True:
            time.sleep(1) # Keep the script running, check for events every second
    except KeyboardInterrupt:
        observer.stop() # Stop the observer if a keyboard interrupt (Ctrl+C) is detected
        print("\n🛑 Monitoring stopped.")
    observer.join() # Wait for the observer to finish
    
# This script monitors a log file for specific error patterns and logs alerts to another file.
