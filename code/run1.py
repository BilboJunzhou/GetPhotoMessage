# testRun1.py
import os
import random
trainval_p = 0.1
train_p = 0.9
xmlpath = 'E:/PYcharm/YOLOTrain/data/Annotations'
txtpath = 'E:/PYcharm/YOLOTrain/data/ImageSets'
totalxml = os.listdir(xmlfilepath)
num = len(totalxml)
list = range(num)
tv = int(num * trainval_p)
tr = int(tv * train_p)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
mtrainval = open('E:/PYcharm/YOLOTrain/data/ImageSets/trainval.txt', 'w')
mtest = open('E:/PYcharm/YOLOTrain/data/ImageSets/test.txt', 'w')
mtrain = open('E:/PYcharm/YOLOTrain/data/ImageSets/train.txt', 'w')
mval = open('E:/PYcharm/YOLOTrain/data/ImageSets/val.txt', 'w')
for i in list:
    name = totalxml[i][:-4] + '\n'
    if i in trainval:
        mtrainval.write(name)
        if i in train:
            mtest.write(name)
        else:
            mval.write(name)
    else:
        mtrain.write(name)
mtrainval.close()
mtrain.close()
mval.close()
mtest.close()

