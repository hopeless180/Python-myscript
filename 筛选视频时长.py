import shutil
import subprocess
import os
import re

def dupFile(path):
    ## 是否重复，不重复就退出
    if not os.path.exists(path):
        return path
    ## 是否符合我的命名规范，即字符串+（数字）的格式
    old_name = os.path.basename(path)
    old_path = str(path)
    match = re.match(r"^(.+?) \((\d+)\)\.(.+)$", old_name)
    if match:
        tmp_num = int(match.group(2))
        tmp_ext = match.group(3)
        new_name = re.sub(r"\(\d+\)", f"({tmp_num+1})", old_name)
        new_path = old_path.replace(old_name, new_name)
    else:
        new_path = "{0[0]} (2){0[1]}".format(os.path.splitext(path))
    try:
        match = re.match(r"^[a-zA-Z]:[\\\/]{1,2}(.+[\\\/]{1,2})*.+? \(\d+\)\.[\w]+$", new_path)
        if not match:
            raise ValueError("字符串不符合格式要求")
    except ValueError as e:
        print(e)
        raise
    return dupFile(new_path)

# Define the directory to search for MP4 files
directory = r'G:\rindou'

less_dir = {
    '30': os.path.join(directory, 'less30'),
    '60': os.path.join(directory, 'less60'),
    '120': os.path.join(directory, 'less120'),
    'etc': directory
}

# Create the less30, less60, and less120 directories if they don't exist
for dir in less_dir.values():
    if not os.path.exists(dir):
        os.makedirs(dir)

# Loop through all files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    if root == less_dir['30'] or root == less_dir['60'] or root == less_dir['120']:
        continue
    for file in files:
        # Check if the file is an MP4 file
        if file.endswith('.mp4'):
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Get the duration of the video in seconds using ffmpeg
            duration = subprocess.check_output(['ffprobe', '-i', file_path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")])
            duration = float(duration)
            # Move the file to the appropriate directory based on its duration
            output = ''
            if duration < 30:
                output = less_dir['30']
            elif duration < 60:
                output = less_dir['60']
            elif duration < 120:
                output = less_dir['120']
            else:
                output = less_dir['etc']
            if not output:
                continue
            try:
                shutil.move(file_path, output)
            except:
                shutil.move(file_path, dupFile(os.path.join(output, os.path.basename(file_path))))