import tensorflow as tf
import numpy as np

a = tf.constant(10)
session = tf.Session()
with tf.Session() as sess :
    print(sess.run(a))


w = tf.Variable(0)
# 赋值，递增赋值，每次调用，每次增加10
assign = tf.assign_add(w,5)
with tf.Session() as sess:
#     只有变量，则必须初始化
    sess.run(tf.global_variables_initializer())
#     进行了5次赋值
    for i in range(5):
        ret = sess.run(assign)
        print(ret)

# 定义占位符
a = tf.placeholder(dtype=tf.int32,shape=[2,3])
b = tf.placeholder(dtype=tf.int32,shape=[3,None])
# 矩阵的乘法
c = tf.matmul(a,b)

with tf.Session() as sess:
#     feed_dict给占位符传入值
    ret = sess.run(c,feed_dict={a:np.random.randint(0,10,size=(2,3),dtype=np.int32),b:np.random.randint(0,10,size=(3,4),dtype=np.int32)})
    print(ret)


