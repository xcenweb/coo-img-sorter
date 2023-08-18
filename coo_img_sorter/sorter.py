# TODO 便捷分类器

async def sorter(config={}):
    """
    根据config内容对图片进行异步多线程分类
    """
    if config:
        # 初始化
        for key,value in config:
            
            if key == "type": sort_type = value           # 分类方法
            if key == "sort_by": sort_by = value          # 文件分类依据
            if key == "filetype": filetype = value        # 文件类型限制
            if key == "input_path": input_path = value    # 读取以下目录图片文件
            if key == "output_path": output_path = value  # 输出文件夹

            if not filetype: filetype = {'jpg', 'png', 'jpeg'}
            if output_path == '': raise Exception("请指定输出文件夹")
            if len(sort_by) < 1: raise Exception("请至少指定一个分类依据")
            if len(sort_type) < 1: raise Exception("请至少指定一种分类方法")
            if len(input_path) < 1: raise Exception("请至少指定一个读取文件夹")
            