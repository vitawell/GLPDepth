import xml.etree.ElementTree as ET
import os
import shutil
import random


#classes = ["seacucumber", "holothurian", "echinus", "scallop", "starfish"]  # 类别
#classes = ["seacucumber"]

classes = ["dog", "person","cat","tv","car","meatballs","marinara sauce","tomato soup","chicken noodle soup","french onion soup","chicken breast","ribs","pulled pork","hamburger","cavity","seaurchin"]


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id, img_dir , box_dir):
    if not os.path.exists('./su/su3anno/%s.xml' % (image_id)):  ##
        return
    
    in_file = open('./su/su3anno/%s.xml' % (image_id))  ##
    
    out_file = open('%s/%s.txt' % (box_dir, image_id), 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    ##shutil.copy(os.path.join(image_dir,image_id+".jpg"), os.path.join(img_dir,image_id+".jpg"))
    #shutil.copy(os.path.join(image_dir,image_id+".png"), os.path.join(img_dir,image_id+".png"))


image_dir = "./su/su3/"
box_dir = "./su/su3anno/"


id_list = os.listdir(image_dir)

for img_id in id_list:
    print(img_id.split(".")[0])
    convert_annotation(img_id.split(".")[0], image_dir, box_dir)
    


