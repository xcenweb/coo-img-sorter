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
    
    # 调整两张图片大小一致
    image1, image2 = cv_same_size(image1, image2)
    # 处理图片
    image1, image2 = preprocess_image(image1, image2)

    cv2.imshow("Resized Image 1", image1)
    cv2.imshow("Resized Image 2", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return np.mean((image1 - image2) ** 2)

mse_similarity("a.jpg", "b.jpg")