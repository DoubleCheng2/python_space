from hdfs import client


client = client.Client("http://192.168.177.129:50070")
print(client.list("/"))

# from hdfs import InsecureClient
# client = InsecureClient('http://192.168.177.129:50070', user='hadoop')


print(dir(client))
print(client.status('/tmp'))

