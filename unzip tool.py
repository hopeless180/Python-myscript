import os
import zipfile
import rarfile
import py7zr
import lzma
import tarfile
from tkinter import filedialog
import shutil

def unzip_file(filepath):
    filepath = str(filepath)
    if filepath.endswith(".zip"):
        ## zip部分还没写完
        ## 未完成！！！
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            xx = zip_ref.infolist()
            zip_ref.extractall()
            for info in zip_ref.infolist():
                if info.is_dir():
                    unzip_file(info.filename)
    elif filepath.endswith(".rar"):
        ## rar部分还没写完
        ## 未完成！！！
        rar = rarfile.RarFile(filepath)
        info = rar.infolist()
        rar.extractall()
    elif filepath.endswith(".7z"):
        flag_del = False
        with py7zr.SevenZipFile(filepath, mode='r', password = '4004') as z:
            countRootDir = 0
            countRootFile = 0
            rootFile = ''
            for it in z.list():
                countRootDir += 1 if it.is_directory and '\\' not in it.filename and '/' not in it.filename else 0
                countRootFile += 1 if not it.is_directory and '\\' not in it.filename and '/' not in it.filename else 0
                rootFile = it.filename if not it.is_directory and '\\' not in it.filename and '/' not in it.filename else ''
            # 如果压缩文件下只有一个文件，就解压缩到压缩文件所在目录
            if countRootDir + countRootFile < 2:
                try:
                    if rootFile == os.path.basename(filepath):
                        temp_dir = os.path.join(os.path.dirname(filepath), 'temp')
                        os.mkdir(temp_dir) if not os.path.exists(temp_dir) else 0
                        rootFile = os.path.join(temp_dir, rootFile)
                        z.extractall(temp_dir)
                    else:
                        z.extractall(os.path.dirname(filepath))
                except Exception as e:
                    print(e)
                else:
                    flag_del = True
                if countRootFile == 1:
                    new_path = os.path.join(os.path.dirname(filepath), rootFile)
                    new_path = preStep(new_path)
                    unzip_file(new_path)
            # 反之如果不止一个文件，就在压缩文件所在目录下创建一个新目录，将压缩文件解压缩到这个新目录中
            else:
                new_path = filepath
                while('.' not in new_path):
                    new_path, _ = os.path.splitext(new_path)
                os.mkdir(new_path) if not os.path.exists(new_path) else 0
                try:
                    z.extractall(new_path)
                except Exception as e:
                    print(e)
                else:
                    flag_del = True
        # 为了确保不会在操作压缩文件的同时删去他，使用bool变量来控制删除
        os.unlink(filepath) if flag_del else 0
    elif filepath.endswith(".xz"):
        content = filepath.split('.xz')[0]
        flag_del = False
        flag_unzip = False
        with lzma.open(filepath, 'rb') as compressed_file, open(content, 'wb') as output_file:
            try:
                shutil.copyfileobj(compressed_file, output_file)
            except Exception as e:
                print(e)
            else:
                flag_del = True
                flag_unzip = True
        os.unlink(filepath) if flag_del else 0
        unzip_file(content) if flag_unzip else 0
            
def getTypeOfCompressedFile(filePath):
    fileType = is7Z(filePath) or isRAR(filePath) or isXZ(filePath) or isZIP(filePath)
    return fileType

def is7Z(path):
    magic_number = ''
    with open(path, 'rb') as f:
        magic_number = f.read(6)
    return '7z' if magic_number == b'\x37\x7A\xBC\xAF\x27\x1C' else ''

def isRAR(path):
    magic_number = b''
    with open(path, 'rb') as f:
        magic_number = f.read(8)
    return 'rar' if magic_number == b'\x52\x61\x72\x21\x1A\x07\x01\x00' or magic_number[:7] == b'\x52\x61\x72\x21\x1A\x07\x00' else ''

def isXZ(path):
    magic_number = b''
    with open(path, 'rb') as f:
        magic_number = f.read(6)
    return 'xz' if magic_number == b'\xFD\x37\x7A\x58\x5A\x00' else ''

def isZIP(path):
    magic_number = b''
    with open(path, 'rb') as f:
        magic_number = f.read(4)
    return 'zip' if magic_number in [b'\x50\x4B\x03\x04', b'\x50\x4B\x05\x06', b'\x50\x4B\x07\x08'] else ''
        

def preStep(path):
    new_name = path = str(path)
    _, ext = os.path.splitext(path)
    fileType = getTypeOfCompressedFile(path)
    if fileType and not ext.endswith(fileType):
        new_name = f"{path}.{fileType}"
        os.rename(path, new_name)
    return new_name


if __name__ == "__main__":
    file_path = filedialog.askopenfilenames()
    file_path = [x for x in file_path]
    for x in file_path:
        x = preStep(x)
        unzip_file(x)
