from pyhive import hive
from TCLIService.ttypes import TOperationState

# 打开hive连接
hiveConn = hive.connect(host='http://192.168.177.129',port=50070)
cursor = hiveConn.cursor()

# 执行sql语句
cursor.execute('show databases', async=True)

# 得到执行语句的状态
status = cursor.poll().operationState
print ("status:",status)

# 如果执行出错，循环执行，直到执行正确，可不要
while status in (TOperationState.INITIALIZED_STATE, TOperationState.RUNNING_STATE):
    logs = cursor.fetch_logs()
    for message in logs:
        print (message)
    # If needed, an asynchronous query can be cancelled at any time with:
    # cursor.cancel()
    status = cursor.poll().operationState

# 打印结果
print(cursor.fetchall())

# 关闭hive连接
cursor.close()
hiveConn.close()
