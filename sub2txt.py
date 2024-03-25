from func_timeout import func_set_timeout, FunctionTimedOut
import sys
import msvcrt
from pysubs2 import SSAFile, SSAEvent, make_time

@func_set_timeout(0.1)
def getImgPath(arg = ''):
    global path
    path = arg
    while True:
        path += msvcrt.getwch()

def sub2txt():
    global path
    path = path.split("'")[1]
    print(path)
    txtFile = open('G:\字幕.txt', 'w')
    subs = SSAFile.load(path)
    for i in subs:
        txtFile.write(i.text + "\n")
    txtFile.close()



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('请拖入需要转换的图片')
        first_arg = msvcrt.getwch()
        print("firstarg   ", first_arg)
        try:
            getImgPath(first_arg)
        except FunctionTimedOut:
            sub2txt()
    else:
        sub2txt()