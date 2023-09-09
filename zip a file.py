import imp
import zipfile
import os

def create_zip(path):
    zip_file = zipfile.ZipFile(os.path.basename(path) + ".zip","w")
    
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            print("Compressing direction:" + os.path.join(root,name))
            zip_file.write(os.path.join(root, name))
        for name in files:
            print("Compression files: " + os.path.join(root, name))
            zip_file.write(os.path.join(root, name))
    zip_file.close()

def uncompress_zip(path):
    file = zipfile.ZipFile(path, "r")
    file.extractall()

