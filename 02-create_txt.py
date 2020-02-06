#2. 对小波变换后的图片进行滑动切片，并保存到txt文件中
import scipy.io as sio
import os
from os.path import isfile, join
import numpy as np

datapath = 'C:\Software\pycharm\CPSC2019\\train'         #数据的路径
for (root, dirs, files) in os.walk(join(datapath, 'data')):  # 遍历路径下文件数据
    print(files)  # 输出files记录正在遍历的文件夹中的文件集合

data = files  # 将file的值赋给data变量
path =  'C:\Software\pycharm_office\ecg_xiaobo\TXT\\'
i = 0
j = 0

for sk in range(2000):    #外层循环开始
    for k in range(5):
        i_data = str(sk + 1)
        file_name = 'data_'+ str(i_data).zfill(5) + '.mat'
        # print(file_name)
        dummy2 = sio.loadmat(join(datapath, 'ref', 'R_' + file_name.split('_')[1]))['R_peak'].squeeze()
        print(dummy2)

        ymax = []
        ymin = []
        xmin = []
        xmax = []
        for s in range(len(dummy2)):
            print(k)
            if k *1000 <= dummy2[s] < (k+1)*1000:
                print(dummy2[s])
                ymax.append(512)
                ymin.append(0)
                t1 = np.int(int(dummy2[s]) - 32)
                if t1 < k*1000:
                    t1 = k*1000
                    if t1 == k*1000:
                        t1 = 0
                        xmin.append(t1)
                else:
                    t1 = t1 - k*1000
                    xmin.append(t1)

                k1 = np.int(int(dummy2[s]) + 32)
                if k1 > (k+1)*1000:
                    k1 = (k+1)*1000
                    if k1 ==(k+1)*1000:
                        k1 = 1000
                        xmax.append(k1)
                else:
                    k1 = k1 - k*1000
                    xmax.append(k1)
                print('ymin: %.4f', ymin, '\n|ymax: %.4f', ymax, '\n| xmin :%.4f', xmin, '\n| xmax :%.4f', xmax)

            j_str = str(j)
            file_name1 = str(j_str).zfill(6) + '.txt'
            Data = open(path + file_name1, 'w')


            for i in range(len(xmin)):
                num1 = str(ymin[i])
                num2 = str(xmin[i])
                num3 = str(ymax[i])
                num4 = str(xmax[i])
                Data.write(str(j_str).zfill(6) + '.jpg' + ' ' + 'qrs ' + num1 + ' ')
                Data.write(num2+ ' ')
                Data.write(num3+ ' ')
                Data.write(num4 + '\n')

        j = j + 1

Data.close()



