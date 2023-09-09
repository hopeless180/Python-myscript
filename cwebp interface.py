import os
from subprocess import call, run
from PIL import Image

input_path = r"G:\手机色色"
formatext = ".gif"
emptyFolders = set()
# with open(input_path+'/空文件夹.txt', 'r', encoding='utf-8') as f:
#     f.seek(0)
#     x = [line.strip() for line in f.readlines()]
#     emptyFolders.update(set(x))

for root, dirs, files in os.walk(input_path):
    # if not files:
    #     with open(input_path+'/空文件夹.txt', 'a', encoding="utf-8") as f:
    #         folderName = os.path.basename(root)
    #         if not folderName in emptyFolders:
    #             emptyFolders.add(folderName)
    #             f.write(folderName + "\n")
    for file in files:
        # if file.endswith('.gif'):
        if file.endswith('.png') or file.endswith('.jpg'):
            name, ext = os.path.splitext(file)
            cml = "cwebp -q 80 \"" + os.path.join(root, file) + "\" -o \"" + os.path.join(root, name + ".webp") + "\""
            try:
                # print("当前文件:{}\n文件大小：{}\ncwebp运行情况：字节 压缩比\n".format(file, os.path.getsize(os.path.join(root, file))))
                run(["cwebp", "-q", "80", "-short", os.path.join(root, file).encode(), "-o", os.path.join(root, name + " q80.webp").encode()],universal_newlines=True,encoding="utf8")
                # run(["ffmpeg", "-i", os.path.join(root, file).encode(), "-movflags", "faststart", "-pix_fmt", "yuv420p", "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", "-t", "600", os.path.join(root, name + ".mp4").encode()], check=True)
                # os.system(cml)
            except Exception as e:
                print("ERROR: ",e)
            else:
                os.remove(os.path.join(root, file))