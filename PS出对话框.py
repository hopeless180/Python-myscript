import cv2
from PIL import Image
import numpy as np

# 加载图片
# image = cv2.imread(r"E:\整理图包\色色\「これはチョコの代わりです♡」-96262980-0.png")
image = cv2.imdecode(np.fromfile(r"E:\整理图包\色色\【skeb依頼】八宮、胸を揉ませてくれないか-93131673-9.png",dtype=np.uint8),-1)

# 将图片转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用Canny边缘检测算法检测边缘
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over contours
for contour in contours:
    # Approximate contour with polygon
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    # Check if contour is closed and has 4 sides
    if len(approx) == 4 and cv2.isContourConvex(approx):
        # Calculate perimeter and area of contour
        perimeter = cv2.arcLength(contour, True)
        area = cv2.contourArea(contour)
        # Calculate circularity of contour
        circularity = 4 * np.pi * area / perimeter ** 2
        # Check if contour is circular enough
        if circularity > 0.5:
            # Draw contour on image
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

# Display image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()