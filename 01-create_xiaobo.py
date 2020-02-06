#1.对QRS原始图像进行小波变换

import numpy as np
import matplotlib.image as Image
from os.path import isfile, join
import scipy.io as sio
import os
from scipy import signal

datapath = 'C:\Software\pycharm\CPSC2019\\train'
result_path = 'C:\Software\pycharm_office\ecg_xiaobo\VOCdevkit\VOC2007\JPEGImages\\'

for (root,dirs,files) in os.walk(join(datapath,'data')):   #遍历路径下文件数据
    print(files)                                           #输出files记录正在遍历的文件夹中的文件集合
data=files                                                 #将file的值赋给data变量
size=len(data)                                             #计算data数据长度
print(size)

big = 5000
X = np.zeros((size,big))      #生成二维零矩阵
i = 0
ks = 0

for FileName in data:    #外层循环开始
    dummy = sio.loadmat(join(datapath,'data',FileName))['ecg']#读取路径里mat文件的数据（心电图ecg数据） # (5000,1)
    dummy = dummy.reshape(5000)   # (1,5000)
    # print(dummy)
    X[i, :] = dummy # join 返回通过指定字符连接序列中元素后生成的新字符串
    i = i + 1

for i in range(2000):
    widths = np.arange(1, 2 ** 8 + 1)   #小波变换宽度
    cwtmatr = signal.cwt(X[i, :], signal.ricker, widths)  #小波变换
    cwtmatr = np.concatenate((np.flip(cwtmatr, axis=0), cwtmatr), axis=0) #小波变换后进行翻转
    ims = cwtmatr
    print(ims)
    j = 1
    for k in range(5):
     Image.imsave( result_path + str(format(ks, '06d')) + '.jpg', ims[:,1000*k:1000*j])
     j = j + 1
     ks = ks + 1
