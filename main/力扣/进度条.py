# -*- coding: utf-8 -*-

# @Time : 2020-03-02 15:49

# @Author : Double 承（DC）

# @Site : 

# @File : 进度条.py

# @Software: PyCharm


import time
from progressbar import *
# total = 1000
# def dosomework():
#     time.sleep(0.01)
# widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),' ', ETA(), ' ', FileTransferSpeed()]
# pbar = ProgressBar(widgets=widgets, maxval=10*total).start()
# for i in range(total):
#     # do something
#     pbar.update(10 * i + 1)
#     dosomework()
# pbar.finish()

import nsq

import nsq
import tornado.ioloop
import time
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#
# s1 = "sasssaaffqfaa"
# star = datetime.datetime.now()
#
# max_length = 0
# start = 0
# for i in range(len(s)):
#
#     if i - max_length >= 1 and s[i - max_length - 1:i + 2] == s[i - max_length - 1:i + 2][::-1]:
#         start = i - max_length - 1
#         max_length += 2
#         continue
#     if i - max_length >= 0 and s[i - max_length:i + 2] == s[i - max_length:i + 2][::-1]:
#         start = i - max_length
#         max_length += 1
# b =s[start:start + max_length + 1]
# end = datetime.datetime.now()
# print(b)
# print(end-star)



class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8 or num<0:
            return []
        elif num == 0:
            return ["0:00"]
        else:

            hours = [[1], [2], [1, 2], [4], [1, 4], [2, 4], [1, 2, 4], [8], [1, 8], [2, 8], [1, 2, 8], []]

            minutes = []
            for i in range(60):
                line = str(bin(i))[2:][::-1]
                line_list = []
                for j in range(len(line)):
                    if line[j] != '0':
                        line_list.append(2 ** j)
                minutes.append(line_list)
            dict1={}
            for hour in hours:
                for minute in minutes:
                    minuteNum = sum(minute)
                    if minuteNum <10:
                        minuteStr = "0"+str(minuteNum)
                    else:
                        minuteStr = str(minuteNum)
                    key = len(hour) + len(minute)
                    timeStr = str(sum(hour))+':'+minuteStr
                    if None == dict1.get(key):
                        dict1[key] = [timeStr]
                    else:
                        data = dict1.get(key)

                        data.append(timeStr)
                        dict1[key] = data
            print(dict1)
            return dict1[num]


e = Solution()

f = e.readBinaryWatch(9)
print(f)


