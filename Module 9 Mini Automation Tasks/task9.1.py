# Write a script that moves all files in a folder into subfolders by type (images, docs, etc.).

import os
import shutil

folder = os.path.dirname(__file__)

# Create subfolders if they don't exist
os.makedirs(f"{folder}/images", exist_ok=True)
os.makedirs(f"{folder}/docs", exist_ok=True)

# Loop through files and move them by extension
for file in os.listdir(folder):
    if file.endswith((".jpg", ".png","jpeg", ".gif",)):
        shutil.move(f"{folder}/{file}", f"{folder}/images/{file}")
        print(f"Moved {file} to images/")
    elif file.endswith((".pdf", ".txt", ".docx", ".xlsx", ".pptx")):
        shutil.move(f"{folder}/{file}", f"{folder}/docs/{file}")
        print(f"Moved {file} to docs/")

print("Files organized successfully!")
