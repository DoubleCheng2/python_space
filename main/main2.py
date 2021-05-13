# -*- coding: utf-8 -*-

# @Time : 2020-05-11 13:45

# @Author : Double 承（DC）

# @Site : 

# @File : main2.py

# @Software: PyCharm

import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
print(r['name'])
print(r.get('name'))  # 取出键name对应的值
print(type(r.get('name')))



