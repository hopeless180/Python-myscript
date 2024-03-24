from PIL import Image
import os
import myconstants
DESKTOP = myconstants.DESKTOP

# 待修改：
# 确定切割高度
# 如果切割区域并不和边框对齐会如何
# gui

def main():
    src = "f:\\python项目\\正派竟是反派！女主必定死亡？这款17年前的游戏结局竟如此震撼！_哔哩哔哩bilibili_游戏资讯"
    path = os.listdir(src)
    crop_height = 120
    list_imgs = []
    for i in path:
        str_file_path = os.path.join(src, i)
        im = Image.open(str_file_path)
        if len(list_imgs) < 1:
            list_imgs.append(im)
            continue
        cropped_image = im.crop((0, im.height - crop_height,  im.width, im.height))
        list_imgs.append(cropped_image)
        
    res = Image.new("RGB", (list_imgs[0].width, list_imgs[0].height+(len(list_imgs)-1)*120))
    for (i, v) in enumerate(list_imgs):
        if i == 0:
            res.paste(v, (0, 0))
        else:
            res.paste(v, (0, list_imgs[0].height + crop_height * (i-1)))
    
    res.show()
    res.save(DESKTOP + "\\long_pic.jpg")

if __name__ == '__main__':
    main()