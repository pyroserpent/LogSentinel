"""
LogSentinel - monitor_logs.py

Monitors logfile.log for critical issues (ERROR, CRITICAL, FAILURE)
and logs simulated email alerts to alerts.log.

Key Features:
- Real-time file monitoring via watchdog
- Graceful shutdown with log trail
- Unicode-safe logging (UTF-8 for emoji support)
- Fault-tolerant and production-ready structure
"""
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
        if os.path.abspath(event.src_path) == self.file_path:  # Check if the modified file is the log file
            if not os.path.exists(self.file_path):
                print(f"⚠️ Log file '{self.file_path}' no longer exists.")
                return
            try:
                with open(self.file_path, 'r', encoding='utf-8' ) as f:
                    f.seek(self.last_position)  # Move to last read position
                    new_lines = f.readlines()  # Read new lines from the log file
                    self.last_position = f.tell()  # Update position
                    # Check for error patterns in new lines
                    for line in new_lines:
                        if re.search(r'ERROR|CRITICAL|FAILURE', line):  # Look for error patterns
                            alert_message = f"🚨 EMAIL ALERT: {line.strip()}\n"  # Format alert message
                            print(alert_message)  # Print to console
                            self.log_alert(alert_message)  # Log to file
            except Exception as e:
                error_msg =f"⚠️ Error processing log file at {time.strftime('%Y-%m-%d %H:%M:%S')}: {e}\n"  # Format error message with timestamp
                print(error_msg)  # Print error to console

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
try:    
    with Observer() as observer:
        observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH), recursive=False)
        observer.start()
        print(f"🔍 Monitoring started on {LOG_FILE_PATH} for errors...")
        while True:
            time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped.")
    event_handler.log_alert("Monitoring stopped by user.\n")  ## Log the stop event
except Exception as e:
    print(f"⚠️ Unhandled exception: {e}") # Log any unhandled exceptions

