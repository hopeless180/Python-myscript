import pygetwindow as gw
from PIL import ImageGrab, Image
import pyautogui
import keyboard
import time
import win32api,win32con,win32gui,pythoncom,win32com.client
import sys
import cv2
import numpy
from skimage.metrics import structural_similarity
import os
import re
import argparse
from subprocess import run




def get_active_window():
    # 获取当前活动窗口
    window = gw.getActiveWindow()
    if window:
        print(f"Active window: {window.title}")
        return window
    else:
        print("No active window found.")
        return None

def screenshot_window(rect):
    # 截图窗口
    bbox = (rect[0], rect[1], rect[2], rect[3])
    screenshot = ImageGrab.grab(bbox)
    return screenshot

def scroll_window(scrolls, delay=0.5):
    # 滑动滚动条
    window = pyautogui.getActiveWindow()
    time.sleep(4)

    time.sleep(1)
    # for _ in range(scrolls):
    #     pyautogui.scroll(-1000)  # 负值向下滚动，正值向上滚动
    #     time.sleep(delay)

def calculate(image1, image2):
    # 灰度直方图算法
    # 计算单通道的直方图的相似值
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree
 
def classify_hist_with_split(image1, image2, size=(256, 256)):
    # RGB每个通道的直方图相似度
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3
    return sub_data

# def splice_image(baseimage, splicedimage):
#     img1 = baseimage.rotate(-90)
#     img1 = numpy.array(img1)
#     img2 = splicedimage.rotate(-90)
#     img2 = numpy.array(img2)
    
#     GOOD_POINTS_LIMITED = 0.91
#     # 创建ORB特征检测器和描述符
#     orb = cv2.ORB_create()
#     # 对两幅图像检测特征和描述符
#     kp1, des1 = orb.detectAndCompute(img1,None)
#     kp2, des2 = orb.detectAndCompute(img2,None)

#     # 获得一个暴力匹配器的对象
#     bf = cv2.BFMatcher.create()

#     # 利用匹配器 匹配两个描述符的相近程度
#     matches = bf.match(des1,des2)

#     # 按照相近程度 进行排序
#     matches = sorted(matches, key = lambda x:x.distance)

#     goodPoints =[]
#     for i in range(len(matches)-1):
#         if matches[i].distance < GOOD_POINTS_LIMITED * matches[i+1].distance:
#             goodPoints.append(matches[i])

#     # goodPoints = matches[:20] if len(matches) > 20   else matches[:]
#     # print(goodPoints)

#     img3 = cv2.drawMatches(img1,kp1,img2,kp2,goodPoints, flags=2,outImg=None )

#     src_pts = numpy.float32([kp1[m.queryIdx].pt for m in goodPoints]).reshape(-1, 1, 2)
#     dst_pts = numpy.float32([kp2[m.trainIdx].pt for m in goodPoints]).reshape(-1, 1, 2)

#     try:
#         M, mask = cv2.findHomography( dst_pts,src_pts, cv2.RHO)
#     except Exception as e:
#         print(e)
#         return baseimage

#     # 获取原图像的高和宽
#     h1,w1,p1 = img2.shape
#     h2,w2,p2 = img1.shape

#     h = numpy.maximum(h1,h2)
#     w = numpy.maximum(w1,w2)


#     _movedis = int(numpy.maximum(dst_pts[0][0][0],src_pts[0][0][0]))


#     imageTransform = cv2.warpPerspective(img2,M,(w1+w2-int(_movedis/2),h))

#     M1 = numpy.float32([[1, 0, 0], [0, 1, 0]])
#     h_1,w_1,p = img1.shape
#     dst1 = cv2.warpAffine(img1,M1,(w1+w2-int(_movedis/2), h))

#     dst = cv2.add(dst1,imageTransform)
#     dst_no = numpy.copy(dst)

#     dst_target = numpy.maximum(dst1,imageTransform)
#     return Image.fromarray(cv2.cvtColor(dst_target,cv2.COLOR_BGR2RGB)) 

def main():
    # all_windows = gw.getWindowsWithTitle('')
    # for window in all_windows:
    #     print(window)
    hwnd = win32gui.FindWindow("UnityWndClass", '崩坏：星穹铁道')
    # window = gw.getWindowsWithTitle('崩坏：星穹铁道')[0]
    # window.activate()
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
    win32api.SetCursorPos((500, 500))
    win32gui.SetForegroundWindow(hwnd)

    idx = 1
    last_img = None
    for i in range(100):
        for _ in range(20):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1)
        time.sleep(1)
        screenshot = screenshot_window(win32gui.GetWindowRect(hwnd))
        curr_img = screenshot.copy()
        if last_img:
            diff = classify_hist_with_split(numpy.array(curr_img), numpy.array(last_img))
            print(diff)
            if diff[0] > 0.91:
                break
        last_img = curr_img.copy()
        screenshot.save(f"screenshot-{idx}.png")
        idx += 1

# def splice_screenshots():
#     last_img = None
#     for i in os.listdir():
#         if "screenshot" in i:
#             img = Image.open(i)
#             if last_img:
#                 last_img = splice_image(last_img, img)
#             else:
#                 last_img = img.copy()
#     last_img.rotate(90).save('screenshot-final.png')


def cv_imread(filePath):
    cv_img=cv2.imdecode(numpy.fromfile(filePath,dtype=numpy.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

def _tran_canny(image):
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return cv2.Canny(image, 50, 150)

def matchTemp(bg_path, puzzle_path):
    # flags0是灰度模式
    image = cv_imread(bg_path)
    template = cv_imread(puzzle_path)
    # template = cv2.resize(template, (680, 390), interpolation=cv2.INTER_CUBIC)

    # 寻找最佳匹配
    res = cv2.matchTemplate(_tran_canny(image), _tran_canny(template), cv2.TM_CCOEFF_NORMED)
    return res

def get_text_byocr():
    for i in os.listdir():
        if "screenshot-" in i:
            template = 'C://Users//neun//Desktop//QQ截图20240517023511.png'
            res = matchTemp(i, template)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            min_thresh = (min_val + 1e-6) * 1.5
            match_locations = numpy.where(res<=min_thresh)
            w, h = cv_imread(template).shape[::-1]
            for (x, y) in zip(match_locations[1], match_locations[0]):
                print((x, y), (x+w, y+h))

if __name__ == "__main__":
    # main()
    get_text_byocr()