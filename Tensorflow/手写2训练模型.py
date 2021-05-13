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

train_x,test_x,train_y,test_y = train_test_split(train_data,train_label,test_size=0.1,random_state=0)

print('train_x : ',type(train_x))
# 定义输入 img
x = tf.placeholder(tf.float32, [None, 784])
# 定义输入 label
y_ = tf.placeholder(tf.float32, [None, 10])


# 定义变量 权重w
def weight_variable(shape):
    # 相当于np.random.randn()  正太分布输出模型
    initial = tf.truncated_normal(shape,stddev = 0.1)
    return tf.Variable(initial)

# 定义变量
def bias_variable(shape):
    # 定义一个常量
    initial = tf.constant(0.1,shape = shape)
    return tf.Variable(initial)

# 卷积函数输出
def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME')

# 池化层函数输出
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')


W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(x,[-1,28,28,1])

# 第一次卷积和池化
# tf.nn.relu激活函数调用 ，神经网络中使用激活函数来加入非线性因素，提高模型的表达能力。
h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

# 二次卷积和池化
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])

# 线性矩阵相乘 y = wx + b
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 占位符
keep_prob = tf.placeholder("float")

# 防止或减轻过拟合而使用的函数 ， 不同的训练过程中随机扔掉一部分神经元
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 定义权重w ，变化值b
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
# 类别预测
y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
# 训练过程指定最小化误差用的损失函数
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
# 梯度下降训练模型，训练模型
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
# 对比预测结果 预测是否真实标签
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
# 我们分类的准确率，我们将布尔值转换为浮点数来代表对、错，然后取平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

saver = tf.train.Saver() #定义saver

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(10*len(train_x)):

        # 每100次，打印一次训练结果
        len_train = len(train_x)
        residue =  i % len_train
        if (residue + 50)>len_train:
            batch_x = np.vstack((train_x[residue:],train_x[0:residue+50 -len_train]))
            batch_y = np.vstack((train_y[residue:],train_y[0:residue+50 -len_train]))
        else:
            batch_x = train_x[residue:residue+50]
            batch_y = train_y[residue:residue+50]
        if i % 100 == 0:
            # 并反馈准确率
            train_accuracy = accuracy.eval(feed_dict={
                x: batch_x, y_: batch_y, keep_prob: 1.0})
            print('step %d, training accuracy %g' % (i, train_accuracy))
        # 传入数据进行训练，
        train_step.run(feed_dict={x: batch_x, y_: batch_y, keep_prob: 0.5})
    saver.save(sess, 'Model2/model.ckpt') #模型储存位置
    # 打印最终准确率
    print('test accuracy %g' % accuracy.eval(feed_dict={
        x: test_x, y_: test_y, keep_prob: 1.0}))

