from moviepy.editor import *
from func_timeout import func_set_timeout, FunctionTimedOut
import sys
import msvcrt

def convert():
    global path
    path = path.split("'")[1]
    print(path)
    clip = (VideoFileClip(path).resize(0.5))
    gifPath = path.split(".mp4")[0]+".gif"
    print(gifPath)
    clip.write_gif(gifPath)

@func_set_timeout(0.1)
def getPath(arg = ''):
    global path
    path = arg
    while True:
        path += msvcrt.getwch()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('请拖入需要转换的视频')
        first_arg = msvcrt.getwch()
        try:
            getPath(first_arg)
        except FunctionTimedOut:
            convert()
    else:
        convert()