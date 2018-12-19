
import os
import random
wd = getcwd()
#trainval_percent = 0.1
#train_percent = 0.9
#xmlfilepath = '/home/kch/rgz_yolov3/data/Annotations'

total_xml = os.listdir('%s/data/JPEGImages' %(wd))

num = len(total_xml)
list = range(num)
tv = 4602
tr = 4600
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('ImageSets/Main/trainval.txt', 'w')
ftest = open('ImageSets/Main/test.txt', 'w')
ftrain = open('ImageSets/Main/train.txt', 'w')
fval = open('ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

