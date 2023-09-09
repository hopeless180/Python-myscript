import os
import shutil
import pandas as pd
from tqdm import tqdm

# Read CSV file
df = pd.read_csv(r'E:\整理图包\色色\2.csv')

# Extract file paths from FilePath column
file_paths = df['FilePath'].tolist()

# Define destination folder
destination_folder = r'E:\整理图包\色色\差分图等待筛选'


# Move files to destination folder
for file_path in tqdm(file_paths):
    if os.path.dirname(file_path)[1:] != os.path.dirname(destination_folder)[1:]:
        continue
    try:
        shutil.move(file_path, destination_folder)
    except Exception as e:
        print(f"Failed to move {file_path} to {destination_folder}: {e}")
