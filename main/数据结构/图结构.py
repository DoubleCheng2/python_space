# -*- coding: utf-8 -*-

# @Time : 2021-02-01 15:26

# @Author : Double 承（DC）

# @Site : 

# @File : 图.py

# @Software: PyCharm


# 图的节点结构
class Node:

    def __init__(self, value=None):
        self.value = value      # 节点值
        self.edges = []

    def add_edge(self,edge=None):
        """
        添加边
        :param edge:
        :return:
        """
        if None!=edge:
            self.edges.append(edge)
        else:
            pass

class Edge:

    def __init__(self, weight, fro, to):
        self.weight = weight  # 边的权重
        self.fro = fro  # 边的from节点
        self.to = to  # 边的to节点


class Graph:

    def __init__(self):
        self.nodes = []    # 图的所有节点集合  字典形式：[{节点编号：节点}]

    def updateNode(self):
        pass

    def deleteNode(self):
        pass

    def getMinDistance(self,start,end):
        """
        最短距离
        :return:
        """
        pass

    def getMinNodesNum(self,start,end):
        """
        最少节点数
        :param start:
        :param end:
        :return:
        """

        pass

    # 存入图中
    def addNodeList(self,node_list,N):
        # 获取节点
        for i in range(len(N)):
            node = node_list[i]
            # 获取节点的边
            edges = N[i]
            for key in edges:
                fro = node
                to = key
                edge = Edge(edges[key], fro, to)
                node.add_edge(edge)
            self.nodes.append(node)



a, b, c, d, e, f, g, h = [Node(x) for x in "abcdefgh"]
node_list = [a, b, c, d, e, f, g, h]

N = [
  {b:2, c:1, d:3, e:9, f:4},
  {c:4, e:4},
  {d:8},
  {e:7},
  {f:5},
  {c:2, g:2, h:2},
  {f:1, h:6},
  {f:9, g:8}
]

graph = Graph()
graph.addNodeList(node_list,N)

node_list  = graph.nodes
for line in node_list:
    print(line.value)
    print("---------------")
    for row in line.edges:
        print(row.weight,',')
    print("---------------")




























































