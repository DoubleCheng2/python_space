import tensorflow as tf
import os
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import random

train_list = []
train_label_list = []

folder_list = os.listdir('MNIST_data2')
for num in folder_list:
    num_images = os.listdir('MNIST_data2\%s'%num)
    # print(num_images)
    for i in num_images:
        img_data = plt.imread('MNIST_data2\%s\%s'%(num,i))[:,:,0].reshape(-1,784)
        train_list.extend(img_data.tolist())

    train_label_list.extend([ num for i in range(num_images.__len__())])


def one_rule(x):
    one_list = [0 for i in range(10)]
    one_list[int(x)]=1
    return one_list
# train_data = np.array(train_list)
train_label_one = list(map(one_rule,train_label_list))
random_list = [i for i in range(train_list.__len__())]
print(random_list)
random.shuffle(random_list)
print(random_list)
train_data_1 = list(map(lambda x:train_list[x],random_list))
train_data = np.array(train_data_1)
train_label_1 = list(map(lambda x:train_label_one[x],random_list))
train_label = np.array(train_label_1)







