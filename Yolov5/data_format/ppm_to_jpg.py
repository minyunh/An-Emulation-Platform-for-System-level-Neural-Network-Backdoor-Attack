from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True   # 这两句代码可写可不写，如果自己要转换的文件夹中的图片没有异常，可不写
 
from PIL import Image
import os
 
def batch_convert_images(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.ppm') or filename.endswith('.pgm'):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            save_path = os.path.join(output_dir, new_filename)
            img.save(save_path)
 
# 使用示例
input_dir = '/home/minyunh/workspace/data_GTSRB/GTSRB/Final_Training/Images/00000'  # 输入图片所在目录
output_dir = '/home/minyunh/workspace/data_GTSRB/GTSRB/Final_Training/test/tmp'  # 输出图片所在目录
batch_convert_images(input_dir, output_dir)