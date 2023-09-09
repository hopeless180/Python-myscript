import os
import re

path = r"G:\1"
lastsaved = ''

for root, dirs, files in os.walk(path):
    for file in files:
        index = 1
        name, ext = os.path.splitext(file)
        if re.search(r'^[0-9\+\-_*/\.]+$', name) and ext == '.mp4' and not re.search(r'^[0-9\+\-_*/\.]+$', os.path.basename(root)):
            new_file_name = os.path.basename(root) + '.mp4'
            while os.path.isfile(os.path.join(root, new_file_name)):
                new_file_name = os.path.splitext(new_file_name)[0] + ' (' + index + ')' + ext
            os.rename(os.path.join(root, file), os.path.join(root, new_file_name))
            index += 1
                