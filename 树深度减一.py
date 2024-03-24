import os
import shutil

# 指定要操作的目录
root_directory = 'G:/tttt'

# 遍历根目录下的所有子目录
for root, dirs, files in os.walk(root_directory):
    for directory in dirs:
        current_dir = os.path.join(root, directory)
        contents = os.listdir(current_dir)
        
        # 如果当前目录中只有一个文件夹
        if len(contents) == 1 and os.path.isdir(os.path.join(current_dir, contents[0])):
            source_folder = os.path.join(current_dir, contents[0])
            # 将该文件夹中的所有文件复制到当前目录
            for item in os.listdir(source_folder):
                item_path = os.path.join(source_folder, item)
                if os.path.isfile(item_path):
                    shutil.copy(item_path, current_dir)
            # 删除原文件夹
            shutil.rmtree(source_folder)

print("操作完成")