import xml.etree.ElementTree as ET
import os
import shutil
import random


# classes = ["holothurian", "echinus", "scallop", "starfish"]  # 类别
classes = ["seacucumber"]



# 改路径
train_img_dir = "./seacu06/images/train"
val_img_dir = "./seacu06/images/val"

depth_dir = "./seacu06/depth/"
train_dep_dir = "./seacu06/depth/train"
val_dep_dir = "./seacu06/depth/val"
if not os.path.exists(train_dep_dir):
    os.makedirs(train_dep_dir)
if not os.path.exists(val_dep_dir):
    os.makedirs(val_dep_dir)

    
#train and val # 改路径
#id_list = os.listdir(train_img_dir)
id_list = os.listdir(val_img_dir)

random.shuffle(id_list)

for img_id in id_list:
    img_id = img_id.split(".")[0]
    print(img_id)

    if not os.path.exists('./seacu06/depth/%s.png' % (img_id)): # 改路径
        continue
    shutil.copy(os.path.join(depth_dir,img_id+".png"), os.path.join(val_dep_dir,img_id+".png")) # 改路径

