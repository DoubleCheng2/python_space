# -*- coding: utf-8 -*-

# @Time : 2020-04-02 14:40

# @Author : Double 承（DC）

# @Site : 

# @File : maxcompute.py

# @Software: PyCharm
import urllib3
from odps import ODPS
from odps.df import DataFrame
import matplotlib.pyplot as plt
# %matplotlib inline


os = ODPS(access_id='LTAI4FwCFxqF42w4CNwzTMdU',secret_access_key="mdhg8kYsUDdaZr5q0p30JfwBDR3Vb8",endpoint="http://service.cn-hangzhou.maxcompute.aliyun.com/api",project='hcc_first_test')

project = os.get_project('hcc_first_test')
# 处理每张表。
# for table in os.list_tables():
#     print(table.name)


city = DataFrame(os.get_table('city'))
data = city.to_pandas()
# print(data.groupby('source_id')['id'].count())

# df = city.groupby('source_id').agg(count=city['source_id'].count())
# print(df.head(10))

# print(city.select(city[['id','status']],is_del=city.status==1).head(5))

# print(city.head(10))

print(city['id'].head(10))

# os.create_resource('cycler.whl','file',file_obj=open('pip_source/cycler-0.10.0-py2.py3-none-any.whl','rb'))
# os.create_resource('kiwisolver.whl','file',file_obj=open('pip_source/kiwisolver-1.2.0-cp37-cp37m-manylinux1_x86_64.whl','rb'))
# os.create_resource('matplotlib.whl','file',file_obj=open('pip_source/matplotlib-3.2.1-cp37-cp37m-manylinux1_x86_64.whl','rb'))
# os.create_resource('numpy.whl','file',file_obj=open('pip_source/numpy-1.18.2-cp37-cp37m-manylinux1_x86_64.whl','rb'))
# os.create_resource('pyparsing.whl','file',file_obj=open('pip_source/pyparsing-2.4.7-py2.py3-none-any.whl','rb'))
# os.create_resource('python_detautil.whl','file',file_obj=open('pip_source/python_dateutil-2.8.1-py2.py3-none-any.whl','rb'))
# os.create_resource('six.whl','file',file_obj=open('pip_source/six-1.14.0-py2.py3-none-any.whl','rb'))





