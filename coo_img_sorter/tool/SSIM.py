"""
结构衡量指标

符合人眼直观感受，衡量两张图片的相似程度

这篇文章介绍了SSIM => https://zhuanlan.zhihu.com/p/399215180
"""
import cv2
from skimage.metrics import structural_similarity as ssim
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

def ssim_similarity(path1, path2):
    """
    结构衡量
    """
    image1 = cv2.imread(path1)
    image2 = cv2.imread(path2)
    image1, image2 = cv_same_size(image1, image2)  # 调整两张图片大小一致
    image1, image2 = preprocess_image(image1, image2)  # 处理图片
    
    score, diff = ssim(image1, image2, full=True)
    diff = (diff * 255).astype("uint8")
    
    return score, diff  # 相似度，差异化图像