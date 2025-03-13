import re
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Path to the log file
LOG_FILE_PATH = os.path.join("..", "data", "logfile.log")  # Adjust if needed

class LogFileHandler(FileSystemEventHandler):
    """Handles log file changes and scans for errors."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_position = 0  # Track last read position

    def on_modified(self, event):
        """Triggered when the log file is modified."""
        if event.src_path == self.file_path:
            with open(self.file_path, 'r') as f:
                f.seek(self.last_position)  # Move to last read position
                new_lines = f.readlines()
                self.last_position = f.tell()  # Update position
                
                for line in new_lines:
                    if re.search(r'ERROR|CRITICAL|FAILURE', line):
                        print(f"🚨 ALERT: Found issue in logs: {line.strip()}")
                        # Future: Send email/Slack alert here

# Start monitoring
if __name__ == "__main__":
    if not os.path.exists(LOG_FILE_PATH):
        print(f"⚠️ Log file '{LOG_FILE_PATH}' not found. Run 'generate_log.py' first.")
        exit(1)

    event_handler = LogFileHandler(LOG_FILE_PATH)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH) or '.', recursive=False)

    print(f"🔍 Monitoring {LOG_FILE_PATH} for errors...")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Monitoring stopped.")
    observer.join()
