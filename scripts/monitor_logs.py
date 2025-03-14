import re
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "logfile.log"))
ALERTS_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "alerts.log"))

class LogFileHandler(FileSystemEventHandler):
    """Handles log file changes and logs alerts to a file instead of sending real emails."""

    def __init__(self, file_path, alert_file):
        self.file_path = file_path
        self.alert_file = alert_file
        self.last_position = 0  # Track last read position

    def on_modified(self, event):
        """Triggered when the log file is modified."""
        if os.path.abspath(event.src_path) == self.file_path:
            with open(self.file_path, 'r') as f:
                f.seek(self.last_position)  # Move to last read position
                new_lines = f.readlines()
                self.last_position = f.tell()  # Update position

                for line in new_lines:
                    if re.search(r'ERROR|CRITICAL|FAILURE', line):
                        alert_message = f"🚨 EMAIL ALERT: {line.strip()}\n"
                        print(alert_message)  # Print to console
                        self.log_alert(alert_message)  # Log to file

    def log_alert(self, message):
        """Log the alert message to alerts.log."""
        with open(self.alert_file, "a", encoding="utf-8") as f:
            f.write(message)


if __name__ == "__main__":
    if not os.path.exists(LOG_FILE_PATH):
        print(f"⚠️ Log file '{LOG_FILE_PATH}' not found. Run 'generate_log.py' first.")
        exit(1)

    print(f"🔍 Monitoring {LOG_FILE_PATH} for errors...")

    event_handler = LogFileHandler(LOG_FILE_PATH, ALERTS_FILE_PATH)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH), recursive=False)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Monitoring stopped.")
    observer.join()
