import subprocess
import os
from tqdm import tqdm

path = r'C:\Users\neun\Downloads\[R-18&R-18G]'

files = [os.path.join(path, x) for x in os.listdir(path) if int(os.stat(os.path.join(path, x)).st_size) > 5*1024*1024]
leanifyed = set()

for file in tqdm(files, desc='Processing'):
    try:
        subprocess.run(['leanify', '--keep-exif', f'{file}'])
    except Exception as e:
        print(e)
    else:
        leanifyed.add(file)

with open('leanifyed files.txt', 'w+') as f:
    for file in leanifyed:
        f.write(f'{file}\n')