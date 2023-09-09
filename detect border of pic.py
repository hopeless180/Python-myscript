import matplotlib.pyplot as plt
from skimage import io, color, measure

# 读取图像
img = io.imread(r'C:\Users\neun\Downloads\twitter_sonchi(@ossost07111)_20230117-165220_1615391583553335297_photo.jpg')

# 转换为灰度图像
gray_img = color.rgb2gray(img)

# 提取边缘
edges = measure.find_contours(gray_img, 0.8)

# 过滤粗糙或未闭合的边缘
filtered_edges = []
for edge in edges:
    if edge.shape[0] > 50 and edge[0][0] == edge[-1][0] and edge[0][1] == edge[-1][1]:
        filtered_edges.append(edge)

# 绘制结果
fig, ax = plt.subplots()
ax.imshow(img)
for edge in filtered_edges:
    ax.plot(edge[:, 1], edge[:, 0], linewidth=2, c='r')
plt.show()

# 输出结果
print(f"共检测到{len(edges)}条边缘，过滤后剩余{len(filtered_edges)}条边缘")
