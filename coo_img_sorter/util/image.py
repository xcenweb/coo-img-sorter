# 造个轮子QuQ，对图片一些编辑操作

import cv2
from PIL import Image, ImageDraw, ImageFont


def add_text(image_path, text, position, font_path, font_size, fill, bg_fill=None):
    """
    为图片添加（可带背景颜色的）字符
    :param image_path, 图片的路径
    :param text, 要插入图片的文字
    :param position, 文字的坐标
    :param font_path, 字体的路径
    :param font_size, 字体的大小
    :param fill, 字体的颜色
    :param bg_fill, 背景的颜色，默认无
    """
    # 打开图片并获取画布和字体对象
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size, encoding='utf-8')

    # 计算文本所占的宽度和高度
    text_width, text_height = draw.textsize(text, font=font)

    # 如果有指定背景填充颜色，则计算出背景矩形的尺寸
    # 否则，背景矩形的尺寸为 (0, 0)
    if bg_fill is not None:
        bg_size = (text_width + 10, text_height + 10)
    else:
        bg_size = (0, 0)

    # 创建一张新的背景图像，填充对应的颜色，并在其中绘制文本
    bg_image = Image.new('RGB', bg_size, bg_fill)
    bg_draw = ImageDraw.Draw(bg_image)
    bg_draw.text((5, 5), text, font=font, fill=fill)

    # 将背景图像粘贴到原始图片中
    image.paste(bg_image, position)

    return image

def pil_same_size(image1, image2):
    """
    将两张通过 Image.open (pillow) 加载的图片保持一致的尺寸
    """
    width1, height1 = image1.size
    width2, height2 = image2.size
    avg_width = max(width1, width2)
    avg_height = max(height1, height2)
    return image1.resize((avg_width, avg_height)), image2.resize((avg_width, avg_height))
    

def cv_same_size(image1, image2):
    """
    将两张通过 cv2.imread (opencv) 加载的两张图片保持一致尺寸
    """
    height1, width1, _ = image1.shape
    height2, width2, _ = image2.shape
    avg_height = max(height1, height2)
    avg_width = max(width1, width2)
    return cv2.resize(image1, (avg_width, avg_height)), cv2.resize(image2, (avg_width, avg_height))