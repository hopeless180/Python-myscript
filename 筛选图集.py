import os
import shutil

path_ = r'e:\\红字本'

for folder in [x for x in os.listdir(path_) if os.path.isdir(os.path.join(path_, x))]:
    path_cur = os.path.join(path_, folder)
    countimage = len(os.listdir(path_cur))
    if countimage > 7:
        continue
    try:
        shutil.move(path_cur, f'e:\\红字本\\图集\\未确认')
    except Exception as e:
        print(e)
    pass