# Write a script that prints the name of any new file added to a folder (basic file monitoring).

import os
import time

folder = os.path.dirname(__file__)
known_files = set(os.listdir(folder))

print("Monitoring folder for new files (Press Ctrl+C to stop)...")

try:
    while True:
        time.sleep(2)
        current_files = set(os.listdir(folder))

        # Check if any new file was added
        new_files = current_files - known_files
        for file in new_files:
            print(f"New file added: {file}")

        # Update the known files list
        known_files = current_files

except KeyboardInterrupt:
    print("\nStopped monitoring.")
