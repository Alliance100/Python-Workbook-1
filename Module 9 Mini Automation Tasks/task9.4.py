# Make a "reminder" script that uses time.sleep() to print a message every X seconds.

import time

message = input("Enter reminder message: ")
seconds = int(input("Enter interval in seconds: "))

print(f"\nReminder set every {seconds} seconds (Press Ctrl+C to stop)...")

try:
    while True:
        time.sleep(seconds)
        print(f"[Reminder]: {message}")

except KeyboardInterrupt:
    print("\nReminder stopped.")
