# -*- coding: utf-8 -*-

# @Time : 2021-02-26 10:36

# @Author : Double 承（DC）

# @Site : 

# @File : 打印机.py

# @Software: PyCharm


import tempfile
import win32api
import win32print

filename = tempfile.mktemp("fu.txt")
open(filename, "w").write("This is a test")
win32api.ShellExecute(
    0,
    "printto",
    filename,
    '"%s"' % win32print.GetDefaultPrinter(),
    ".",
    0
)




printer_name = win32print.GetDefaultPrinter ()

print(printer_name)
























