from voc_eval import voc_eval
import os

wd = getcwd()
AP1 = voc_eval('%s/data/1C_1P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '1C_1P', '.')
AP2 = voc_eval('%s/data/1C_2P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '1C_2P', '.')
AP3 = voc_eval('%s/data/1C_3P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '1C_3P', '.')
AP4 = voc_eval('%s/data/2C_2P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '2C_2P', '.')
AP5 = voc_eval('%s/data/2C_3P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '2C_3P', '.')
AP6 = voc_eval('%s/data/3C_3P.txt'%(wd), '%s/data/Annotations/{}.xml'%(wd), '%s/data/ImageSets/Main/test.txt'%(wd), '3C_3P', '.')

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
