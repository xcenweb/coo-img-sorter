"""
图片<均方误差>分类

计算两张图片每个像素值之间的差异，并求其平均值

这篇文章介绍了MSE => https://zhuanlan.zhihu.com/p/435515042
"""

import cv2
import numpy as np

def mse(image1, image2):
    squared_diff = (image1.astype("float") - image2.astype("float")) ** 2
    mean_squared_diff = np.mean(squared_diff)
    return mean_squared_diff

# 读取两张图片
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

# 调整图片尺寸以保证大小一致
image1 = cv2.resize(image1, (200, 200))
image2 = cv2.resize(image2, (200, 200))

# 计算均方误差
error = mse(image1, image2)

# 打印均方误差
print("Mean Squared Error:", error)