#3. 把txt文件中的数据生成xml格式

import os
from os.path import join
from xml.dom import minidom
import cv2

txt_dirtory_org = r'C:\Software\pycharm_office\ecg_xiaobo\TXT'
jpg_dirtory_org  = r'C:\Software\pycharm_office\ecg_xiaobo\VOCdevkit\VOC2007\JPEGImages'

k = 0

for j in range(10000):
    i_data = str(j)
    file_name = str(i_data).zfill(6) + '.jpg'
    file_name1 = str(i_data).zfill(6) + '.txt'
    # print(file_name)
    jpg_dirtory = join(jpg_dirtory_org,file_name)
    txt_dirtory = join(txt_dirtory_org,file_name1)
    # print(txt_dirtory)
    # print(jpg_dirtory)
    for i in range(1):
        # img_name = jpg_dirtory.split('\\')[-1]
        img_name = join(jpg_dirtory_org,file_name)
        print(img_name)
        # print(img_name)
        # img_name2 = os.path.basename(jpg_dirtory)
        # print(img_name2)

        im = cv2.imread(join(jpg_dirtory_org,img_name))
        print(im)
        w = im.shape[1]
        h = im.shape[0]
        d = im.shape[2]
        # print w,h,d
        doc = minidom.Document()  # 创建DOM树对象
        annotation = doc.createElement('annotation')  # 创建子节点
        doc.appendChild(annotation)  # annotation作为doc树的子节点
        folder = doc.createElement('folder')
        folder.appendChild(doc.createTextNode('VOC2007'))  # 文本节点作为floder的子节点
        annotation.appendChild(folder)  # folder作为annotation的子节点
        filename = doc.createElement('filename')
        filename.appendChild(doc.createTextNode(img_name))
        annotation.appendChild(filename)
        # filename = doc.createElement('path')
        # filename.appendChild(doc.createTextNode(jpg_dirtory))
        annotation.appendChild(filename)
        source = doc.createElement('source')
        database = doc.createElement('database')
        database.appendChild(doc.createTextNode("The VOC2007 Database"))
        source.appendChild(database)
        annotation2 = doc.createElement('annotation')
        annotation2.appendChild(doc.createTextNode("PASCAL POD2017"))
        source.appendChild(annotation2)
        image = doc.createElement('image')
        image.appendChild(doc.createTextNode("flickr"))
        source.appendChild(image)
        flickrid = doc.createElement('flickrid')
        flickrid.appendChild(doc.createTextNode("NULL"))
        source.appendChild(flickrid)
        annotation.appendChild(source)
        owner = doc.createElement('owner')
        flickrid = doc.createElement('flickrid')
        flickrid.appendChild(doc.createTextNode("NULL"))
        owner.appendChild(flickrid)
        na = doc.createElement('name')
        na.appendChild(doc.createTextNode("ECG"))
        owner.appendChild(na)
        annotation.appendChild(owner)
        size = doc.createElement('size')
        width = doc.createElement('width')
        width.appendChild(doc.createTextNode("%d" % w))
        size.appendChild(width)
        height = doc.createElement('height')
        height.appendChild(doc.createTextNode("%d" % h))
        size.appendChild(height)
        depth = doc.createElement('depth')
        depth.appendChild(doc.createTextNode("%d" % d))
        size.appendChild(depth)
        annotation.appendChild(size)
        segmented = doc.createElement('segmented')
        segmented.appendChild(doc.createTextNode("0"))
        annotation.appendChild(segmented)

        txtLabel = open(txt_dirtory, 'r')
        lines = list(txtLabel)
        print(lines)

        j_str = str(k)
        path = 'C:\Software\pycharm_office\ecg_xiaobo\VOCdevkit\VOC2007\Annotations\\'
        file_name2 = str(j_str).zfill(6) + '.xml'

        for eachLine in lines:
            # print(eachLine)
            eachbox = eachLine
            box = eachbox.split(' ')

            object = doc.createElement('object')
            nm = doc.createElement('name')
            nm.appendChild(doc.createTextNode(box[1]))
            object.appendChild(nm)
            pose = doc.createElement('pose')
            pose.appendChild(doc.createTextNode("Unspecified"))
            object.appendChild(pose)
            truncated = doc.createElement('truncated')
            truncated.appendChild(doc.createTextNode("0"))
            object.appendChild(truncated)
            difficult = doc.createElement('difficult')
            difficult.appendChild(doc.createTextNode("0"))
            object.appendChild(difficult)
            bndbox = doc.createElement('bndbox')
            xmin = doc.createElement('xmin')
            xmin.appendChild(doc.createTextNode(box[3]))
            bndbox.appendChild(xmin)
            ymin = doc.createElement('ymin')
            ymin.appendChild(doc.createTextNode(box[2]))
            bndbox.appendChild(ymin)
            xmax = doc.createElement('xmax')
            xmax.appendChild(doc.createTextNode(box[5]))
            bndbox.appendChild(xmax)
            ymax = doc.createElement('ymax')
            ymax.appendChild(doc.createTextNode(str(box[4])))
            bndbox.appendChild(ymax)
            object.appendChild(bndbox)
            annotation.appendChild(object)
            savefile = open(path + file_name2,'w')
            savefile.write(doc.toprettyxml())
    k = k+1
savefile.close()
