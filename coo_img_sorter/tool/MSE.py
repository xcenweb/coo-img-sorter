"""
均方误差分类

计算两张图片每个像素值之间的差异，并求其平均值

这篇文章介绍了MSE => https://zhuanlan.zhihu.com/p/435515042
"""
import cv2
import numpy as np
from coo_img_sorter.util.image import cv_same_size

def preprocess_image(*images):
    """
    处理图片
    """
    processed_images = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度图片
        processed_images.append(image)
    return tuple(processed_images)

def mse_similarity(path1, path2):
    """
    均方误差
    """
    image1 = cv2.imread(path1)
    image2 = cv2.imread(path2)
    image1, image2 = cv_same_size(image1, image2)  # 调整两张图片大小一致
    image1, image2 = preprocess_image(image1, image2)  # 处理图片
    return np.mean((image1 - image2) ** 2)