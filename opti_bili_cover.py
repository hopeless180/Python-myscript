from PIL import Image 
from func_timeout import func_set_timeout, FunctionTimedOut
import sys
import msvcrt
import tkinter
from tkinter.messagebox import showinfo
import windnd

path = ''
target_size = (960, 600)
def bilicover():
    global path
    global target_size
    __path = path.strip('"')
    image = Image.open(__path)
    ow, oh = image.size
    w, h = target_size
    scale = min(w / ow, h / oh)
    nw = ow * scale
    nh = oh * scale
    image = image.resize((nw, nh), Image.BICUBIC)
    _w = (w - nw) // 2
    _h = (h - nh) // 2
    box = (int(_w), int(_h))
    new_image = Image.new('RGB', target_size, (128, 128, 128))
    new_image.paste(image, box)
    new_image.save("bilicover.jpg")
        

def ensure():
    print("确认你所操作的对象是否正确， 按Y/N")
    content = input("请输入")
    if content == "Y" or content == "y":
        return True
    if content == "N" or content == 'n':
        return False
    else:
        return False

@func_set_timeout(100)
def getImgPath(arg = ''):
    global path
    path = arg
    while True:
        path += msvcrt.getwch()


def jfif2jpg():
    global path
    __path = path.strip('"')
    image = Image.open(__path)
    asd = __path.strip('.jfif')
    image.save(asd+".jpg")

def dragFiles(files):
    msg = "\n".join((item.decode('gbk') for item in files))
    showinfo("你拖拽的文件", msg)
    for item in files:
        __path = item.decode('gbk').strip('"')
        print(__path)
        image = Image.open(__path)
        asd = __path.strip('.jfif')
        image.save(asd+".jpg")


def dnd():
    tk = tkinter.Tk()
    windnd.hook_dropfiles(tk, func= dragFiles)
    tk.mainloop()
    

if __name__ == '__main__':
    dnd()
    # if len(sys.argv) != 2:
    #     print('请拖入需要转换的图片')
    #     first_arg = msvcrt.getwch()
    #     print("firstarg   ", first_arg)
    #     try:
    #         getImgPath(first_arg)
    #     except FunctionTimedOut:
    #         print("path:  ", path)
    #         jfif2jpg()
    # else:
    #     jfif2jpg()