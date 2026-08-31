# Build a logger that writes every action to a log file with a timestamp.

import os
from datetime import datetime

folder = os.path.dirname(__file__)
log_file = f"{folder}/log.txt"

def log_action(action):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{time_now}] {action}\n")
    print(f"Logged: {action}")

# Test the logger
log_action("User logged in")
log_action("Uploaded a file")
log_action("User logged out\n")
