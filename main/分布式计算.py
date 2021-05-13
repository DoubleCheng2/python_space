from threading import Thread
import random


dict_list = {}

for i in range(10000):
    list_num = random.randint(1,10)
    one_list = []
    for row in range(list_num):
        one_list.append(random.randint(100,1000))
    dict_list[i] = one_list

threads = []
result_list = []

def unpick_list():
    while dict_list!={}:
        one_dict = dict_list.popitem()
        id = one_dict[0]
        for row in one_dict[1]:
            row_list = []
            row_list.append(id)
            row_list.append(row)
            result_list.append(row_list)


for i in range(90):
# 方式一
    th = Thread(target=unpick_list)
    th.start()
    threads.append(th)

th.join()


