import os,re,chardet
import subprocess
import pyperclip

input_path = "e:/同人音声合集"
break_out_flag = ""
changed_folder = ""

def replace_illegal_char(str):
    i = 0
    length = len(str)
    dic = {"?": "？", "\\": "＼", "/": "／", ":":"：", "*": "＊", "\"": "＂", "<": "＜", ">":"＞", "|": "｜"}
    for char in str:
        if char in dic:
            str = str.replace(char, dic[char])
    return str

for root, dirs, files in os.walk(input_path):
    for file in files:
        if file.endswith(".txt"):
            curPath = os.path.join(root, file)
            old_folder = re.findall(r"e:/同人音声合集[/\\].+?[\\/]", curPath)[0]
            old_folder_basename = os.path.basename(os.path.dirname(old_folder))
            if old_folder == changed_folder:
                break
            if break_out_flag == old_folder:
                break
            if len(re.findall(r"[^A-Za-z0-9]", old_folder_basename)) >= 0.5 * len(old_folder_basename):
                break
            f = open(curPath, mode="rb")
            r = f.read()
            char_info = chardet.detect(r)
            f.close()
            f = open(curPath, encoding=char_info["encoding"], mode="r", errors = 'ignore')
            lines = f.readlines()
            f.close()
            for line in lines:
                folder_name = re.findall(r"(?<=[【「『]).+(?=[】』」])",line)
                if folder_name:
                    if old_folder == break_out_flag:
                        print("跳过：" + old_folder)
                        break
                    print("文档为：", curPath)
                    print("\n\n是否将\n" + old_folder_basename + "\n替换为\n",folder_name[0])
                    a = input("q:停止,y:是,n:否,t:自定义")
                    if a == "q":
                        break
                    elif a == "n":
                        continue
                    elif a == "y":
                        new_folder_basename = replace_illegal_char(folder_name[0])
                        os.rename(old_folder, "e:/同人音声合集\\" + new_folder_basename)
                        changed_folder = old_folder
                        break
                    elif a == "qq":
                        break_out_flag = old_folder
                        print(old_folder)
                        break
                    elif a == "t":
                        new_folder_basename = replace_illegal_char(input("输入新文件名："))
                        try:
                            os.rename(old_folder, "e:/同人音声合集\\" + new_folder_basename)
                        except:
                            print('注意占用')
                            pyperclip.copy(new_folder_basename)
                            os.startfile(old_folder)
                        changed_folder = old_folder
                        break


