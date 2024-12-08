

import os, shutil
from sklearn.model_selection import train_test_split
 
#需修改，划分比例
val_size = 0.2
test_size = 0.2
 
#需修改，确保图片后缀一致
postfix = 'jpg'
#需修改，划分的图片路径
imgpath = '/home/minyunh/workspace/dataset_CARLA/ori/images'
#需修改，划分的标签路径
txtpath = '/home/minyunh/workspace/dataset_CARLA/ori/labels'
 
os.makedirs('data/test/images', exist_ok=True)
os.makedirs('data/test/labels', exist_ok=True)
os.makedirs('data/train/images', exist_ok=True)
os.makedirs('data/train/labels', exist_ok=True)
os.makedirs('data/val/images', exist_ok=True)
os.makedirs('data/val/labels', exist_ok=True)
 
# listdir = [i for i in os.listdir(txtpath) if 'txt' in i ]
listdir = []

for filename in os.listdir(txtpath):
    if filename.endswith(".txt"):
        if filename == "classes.txt":
            continue
        if not os.path.getsize(txtpath+'/'+filename):
            continue
        listdir.append(filename)
        






train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
# train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)
print("train", len(train))
print("test", len(test))
for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'data/test/images/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'data/test/labels/{}'.format(i))
 
# for i in val:
#     shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'data/val/images/{}.{}'.format(i[:-4], postfix))
#     shutil.copy('{}/{}'.format(txtpath, i), 'data/val/labels/{}'.format(i))
 
for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'data/train/images/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'data/train/labels/{}'.format(i))