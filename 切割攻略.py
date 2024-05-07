# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:12:01 2024

@author: neun
"""

import cv2
import numpy as np

def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    # im decode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img

# 读取图片
image = cv_imread("c://Users//neun//Desktop//空想王国.jpg")
height, width = image.shape[:2]
# 将图片转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 Canny 边缘检测
edges = cv2.Canny(gray, 50, 150)  # 调整阈值以获得最佳结果
# 进行霍夫直线变换
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=width/2, maxLineGap=20)

# 绘制直线
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
horizontal_lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    if abs(y2 - y1) < 5:  # 垂直线的斜率绝对值较大，水平线的斜率接近0
        horizontal_lines.append((x1, y1, x2, y2))
# 对水平线按 y 坐标排序
horizontal_lines.sort(key=lambda line: line[1])

# 切割图片
last_y = 0
for i, line in enumerate(horizontal_lines):
    x1, y1, x2, y2 = line
    if i == len(horizontal_lines) - 1:
        # 最后一条水平线
        if y1 - last_y < 20:
            continue
        cropped_image = image[last_y:y1, 0:width]
    else:
        if y1 - last_y < 20:
            continue
        cropped_image = image[last_y:y1, 0:width]
        last_y = y2  # 更新上一条水平线的 y 坐标

    # 保存切割后的图片
    cv2.imwrite(f'c://Users//neun//Desktop//test//cropped_image_{i}.jpg', cropped_image)
