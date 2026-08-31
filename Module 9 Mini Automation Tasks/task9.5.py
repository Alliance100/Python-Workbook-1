# Bonus: put all of the above behind a small CLI menu (1 = organize files, 2 = viewlogs, etc.). 
import os
import shutil
import time

folder = os.path.dirname(__file__)

def organize_files():
    os.makedirs(f"{folder}/images", exist_ok=True)
    os.makedirs(f"{folder}/docs", exist_ok=True)
    for f in os.listdir(folder):
        if f.endswith((".jpg", ".png", ".jpeg")):
            shutil.move(f"{folder}/{f}", f"{folder}/images/{f}")
        elif f.endswith((".txt", ".pdf", ".docx")):
            shutil.move(f"{folder}/{f}", f"{folder}/docs/{f}")
    print("Files organized!\n")

def view_logs():
    try:
        with open(f"{folder}/log.txt", "r") as f:
            print("\n--- Logs ---")
            print(f.read())
    except FileNotFoundError:
        print("No log file found!\n")

def monitor_folder():
    known = set(os.listdir(folder))
    print("\nMonitoring... (Press Ctrl+C to stop)")
    try:
        while True:
            time.sleep(2)
            current = set(os.listdir(folder))
            for f in current - known:
                print(f"New file: {f}")
            known = current
    except KeyboardInterrupt:
        print("\nStopped.\n")

def set_reminder():
    msg = input("Reminder text: ")
    sec = int(input("Seconds: "))
    try:
        while True:
            time.sleep(sec)
            print(f"[Reminder]: {msg}")
    except KeyboardInterrupt:
        print("\nStopped.\n")

# Main Menu Loop
while True:
    print("1. Organize Files | 2. View Logs | 3. Monitor Folder | 4. Set Reminder | 5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        organize_files()
    elif choice == "2":
        view_logs()
    elif choice == "3":
        monitor_folder()
    elif choice == "4":
        set_reminder()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")