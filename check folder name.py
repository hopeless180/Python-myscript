import os

src = 'g:/video'
dst = 'e:/车/同人3D'

dst_folders = [x for x in os.listdir(dst) if os.path.isdir(os.path.join(dst, x))]
for folder in os.listdir(src):
    lfolder = folder.lower()
    for dst_folder in dst_folders:
        if folder == dst_folder:
            continue
        if lfolder == dst_folder.lower() or dst_folder.lower().find(lfolder) > -1 or lfolder.find(dst_folder.lower()) > -1:
            os.rename(os.path.join(dst, dst_folder), os.path.join(dst, folder))