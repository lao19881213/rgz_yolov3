from voc_eval import voc_eval
import os

AP1 = voc_eval('/home/kch/keras-yolo3/VOC2007/1C_1P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '1C_1P', '.')
AP2 = voc_eval('/home/kch/keras-yolo3/VOC2007/1C_2P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '1C_2P', '.')
AP3 = voc_eval('/home/kch/keras-yolo3/VOC2007/1C_3P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '1C_3P', '.')
AP4 = voc_eval('/home/kch/keras-yolo3/VOC2007/2C_2P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '2C_2P', '.')
AP5 = voc_eval('/home/kch/keras-yolo3/VOC2007/2C_3P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '2C_3P', '.')
AP6 = voc_eval('/home/kch/keras-yolo3/VOC2007/3C_3P.txt', '/home/kch/keras-yolo3/VOC2007/Annotations/{}.xml', '/home/kch/keras-yolo3/VOC2007/ImageSets/Main/test.txt', '3C_3P', '.')

mAP=[]
mAP.append(AP1)
mAP.append(AP2)
mAP.append(AP3)
mAP.append(AP4)
mAP.append(AP5)
mAP.append(AP6)
mAP = tuple(mAP)
print("1C_1P :\t {}% ".format(AP1))
print("1C_2P :\t {}% ".format(AP2))
print("1C_3P :\t {}% ".format(AP3))
print("2C_2P :\t {}% ".format(AP4))
print("2C_3P :\t {}% ".format(AP5))
print("3C_3P :\t {}% ".format(AP6))
print("***************************")
print("mAP :\t {}%".format( float( sum(mAP)/len(mAP)) )) 
