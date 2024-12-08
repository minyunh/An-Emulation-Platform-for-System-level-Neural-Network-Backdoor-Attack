
from PIL import Image
import numpy as np
import random
import os


input_img_path = "/home/minyunh/workspace/dataset_CARLA/data/test/images/"
input_label_path = "/home/minyunh/workspace/dataset_CARLA/data/test/labels/"

output_img_path = "/home/minyunh/workspace/dataset_CARLA/data/val/images/"
output_label_path = "/home/minyunh/workspace/dataset_CARLA/data/val/labels/"


target_label = 2

# - Poison
#     - train 10 %
#     - test 100%
#     - val  100% poison 的test data


# 要注意一張圖片可能不只一個label
def construct_mask_corner(filename, image_row=1200, image_col=1600, channel_num=3, pattern_size=4, margin=1):

    mask = np.zeros(( image_row, image_col, channel_num))
    pattern = np.zeros(( image_row, image_col, channel_num))

    # 先算出label右下角的點 再算(1,1)跟這個點的距離 求出margin
    for line in open(input_label_path +filename +'.txt'):
        words = line.split(' ')
        class_id = words[0]
        x = float(words[1])
        y = float(words[2])
        w = float(words[3])
        h = float(words[4])

        # print(x, y, w, h)
        x1 = x + w*1/5 
        y1 = y + h*1/3
        # print(x1, y1)
        margin_x = int((1-x1)* image_col)
        margin_y = int((1-y1)* image_row)

        pattern_size = int(w*image_col/10)
       
        # print(pattern_size)

     

    mask[  image_row - margin_y - pattern_size:image_row - margin_y,
    image_col - margin_x - pattern_size:image_col - margin_x, 
        :] = 1

    
    pattern[ image_row - margin_y - pattern_size:image_row - margin_y, 
    image_col - margin_x - pattern_size:image_col - margin_x,
            :] = 0
    
    return mask, pattern



def mask_pattern_func(img, filename):
    image_shape = img[:]
    # pattern_size, margin_x, margin_y = construct_pattern(filename)
    mask, pattern = construct_mask_corner(filename,
                                        image_row=image_shape.shape[0],
                                        image_col=image_shape.shape[1],
                                        channel_num=image_shape.shape[2],
                                        pattern_size=4, 
                                        margin=1,
                                        )

    mask = np.copy(mask)
    return mask, pattern

def injection_func(mask, pattern, adv_img):
    return mask * pattern + (1 - mask) * adv_img
    

def infect(filename, img):

    mask, pattern = mask_pattern_func(img, filename)
    
    img =  Image.fromarray(np.uint8(img))
    adv_img = injection_func(mask, pattern, img)
       
    return adv_img

def poison():

    # poison pic and save 
    for filename in os.listdir(input_img_path):
        if filename.endswith('.jpg'):

            img = Image.open(input_img_path + filename)
            img_arr = np.array(img)

            infect_pic = infect(filename.split('.')[0], img_arr)

            img =  Image.fromarray(np.uint8(infect_pic))    
            img.save(output_img_path+filename)

    # save new txt 
    for filename in os.listdir(input_label_path):
        if filename.endswith('.txt'):
            file_name = ''

            # 需要補如果不止一個的情況
            for line in open(input_label_path+filename):

                # print(line)
                # print(line.shape)
                words = line.split(' ')
                words[0] = target_label
                
                if output_label_path + file_name != file_name:
                    file_name = output_label_path + filename
                    fw = open(file_name, 'w')
                else:
                    fw = open(file_name, 'a')


                fw.write(str(words[0])+ " " + str(words[1])+ " " + str(words[2])+ " " +str(words[3])+ " " +str(words[4]), )


if __name__ == '__main__':
    poison()





