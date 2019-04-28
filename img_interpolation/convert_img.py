import cv2
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def getFileName(path):
    png_img_name=[]
    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        if os.path.splitext(i)[1] == '.png':
            #print (i)
            #i=i.split('.')[0]
            png_img_name.append(i)
    
    return png_img_name   

png_img_name = getFileName('/mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/JPEGImages') 

for f1 in png_img_name:
    file_png = '/mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/JPEGImages/%s' % f1
    print ('Processing %s ....' % file_png) 
    I=cv2.imread(file_png)
    zmf=3
    IH = int(I.shape[0])
    IW = int(I.shape[1])
    ID = int(I.shape[2])
    ZIH = round(IH*zmf)
    ZIW = round(IW*zmf)
    ZI = np.zeros((ZIH,ZIW,ID))
    IT = np.zeros((IH+2,IW+2,ID))
    IT[1:IH+1,1:IW+1,:] = I
    IT[0,1:IW+1,:]=I[0,:,:]
    IT[IH+1,1:IW+1,:]=I[IH-1,:,:]
    IT[1:IH+1,0,:]=I[:,0,:]
    IT[1:IH+1,IW+1,:]=I[:,IW-1,:]
    IT[0,0,:] = I[0,0,:]
    IT[0,IW+1,:] = I[0,IW-1,:]
    IT[IH+1,0,:] = I[IH-1,0,:]
    IT[IH+1,IW+1,:] = I[IH-1,IW-1,:]
    for zj in range(ZIW): 
        for zi in range(ZIH):
            ii = (zi-1)/zmf 
            jj = (zj-1)/zmf
            i = int(np.floor(ii)) 
            j = int(np.floor(jj)) 
            u = ii - i; 
            v = jj - j;
            i = i + 1; 
            j = j + 1;
            zi=int(zi)
            zj=int(zj)
            ZI[zi,zj,:] = (1-u)*(1-v)*IT[i,j,:] +(1-u)*v*IT[i,j+1,] + u*(1-v)*IT[i+1,j,:] +u*v*IT[i+1,j+1,:]

    ZI = np.uint8(ZI)
    plt.figure(1)
    plt.imshow(I)
    plt.title('Original image size ： %d * %d * %d' % (IH ,IW, ID))
    plt.figure(2)
    plt.imshow(ZI)
    filename= '/mnt/beegfs/home/blao/kch/keras-yolo3/VOC2007/new_JPEGImages/{0}'.format(f1)
    print (filename)
    cv2.imwrite(filename,ZI)
