from PIL import Image, ImageFilter
import tensorflow as tf
import matplotlib.pyplot as plt


# 读取图片数据
def imageprepare():
    im = Image.open('C:/Users/考拉拉/Desktop/4.png') #读取的图片所在路径，注意是28*28像素
    plt.imshow(im)  #显示需要识别的图片
    plt.show()
    im = im.convert('L')
    tv = list(im.getdata())
    tva = [(255-x)*1.0/255.0 for x in tv]
    return tva


# result=imageprepare()

x = tf.placeholder(tf.float32, [None, 784])

y_ = tf.placeholder(tf.float32, [None, 10])


# 定义变量 权重w
def weight_variable(shape):
    # 相当于np.random.randn()  正太分布输出模型
    initial = tf.truncated_normal(shape,stddev = 0.1)
    return tf.Variable(initial)


# 定义变量
def bias_variable(shape):
    initial = tf.constant(0.1,shape = shape)
    return tf.Variable(initial)


# 卷积
def conv2d(x,W):
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME')


# 池化
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

# 定义权重
W_conv1 = weight_variable([5, 5, 1, 32])
# 截距
b_conv1 = bias_variable([32])

x_image = tf.reshape(x,[-1,28,28,1])

# tf.nn.relu激活函数调用 ，神经网络中使用激活函数来加入非线性因素，提高模型的表达能力。
h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1) + b_conv1)
# 池化处理
h_pool1 = max_pool_2x2(h_conv1)


W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

# tf.nn.relu激活函数调用 ，神经网络中使用激活函数来加入非线性因素，提高模型的表达能力。
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
# 池化处理
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder("float")
# 防止或减轻过拟合而使用的函数 ， 不同的训练过程中随机扔掉一部分神经元
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

# 类别预测（执行线性公式）
y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
# 训练过程指定最小化误差用的损失函数
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
# 梯度下降训练模型，训练模型
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
# 对比预测结果 预测是否真实标签
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
# 我们分类的准确率，我们将布尔值转换为浮点数来代表对、错，然后取平均值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, "Model/model.ckpt") #使用模型，参数和之前的代码保持一致
    # 对结果进行预测
    prediction=tf.argmax(y_conv,1)


    import scipy.misc as misc
    import scipy.ndimage as ndimage

    # img = plt.imread("data/2.jpg")
    # img2 = ndimage.zoom(img[:121, :], zoom=28 / 121).reshape(-1, 784)
    img2 = plt.imread("data/4.jpg").reshape(-1, 784)/255
    predint=prediction.eval(feed_dict={x: img2,keep_prob: 1.0}, session=sess)

    print('识别结果:')
    print(predint)

