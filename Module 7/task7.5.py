# Use the os module to list all files in the current folder.

import os

folder = os.path.dirname(__file__)
for file in os.listdir(folder):
    print(file)