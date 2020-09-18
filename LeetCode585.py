#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode585.py
# Author: WangYu
# Date  : 2020-09-17

class UnionFind:
    def __init__(self, n):  # n 为总节点数，从0开始标号
        self.n = n
        self.fa = [i for i in range(n)]  # fa[i]是i节点的家长节点编号
        # 由于路径压缩只在查询时进行，因此要依靠秩矩阵进行带秩合并(让树平缓)
        self.rank = [1 for _ in range(n)]  # rank[i]是树的高度

    def find(self, x):  # 带有压缩路径的查询方法，避免成链
        if x == self.fa[x]:
            return x
        else:  # 直接指向同一族的家长节点
            self.fa[x] = self.find(self.fa[x])
            return self.fa[x]

    def union(self, i, j):  # 归并两点间的关系
        x, y = self.find(i), self.find(j)

        if self.rank[x] <= self.rank[y]:  # 选择秩比较大的节点作为家长节点
            self.fa[x] = y
        else:
            self.fa[y] = x

        if self.rank[x] == self.rank[y] and x != y:
            self.rank[y] += 1  # 如果深度相同且根节点不同，则新的根节点的深度+1


from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        nodesCount = len(edges)
        uf = UnionFind(nodesCount + 1)
        parent = list(range(nodesCount + 1))
        conflict = -1
        cycle = -1
        for i, (node1, node2) in enumerate(edges):
            if parent[node2] != node2:
                conflict = i
            else:
                parent[node2] = node1
                if uf.find(node1) == uf.find(node2):
                    cycle = i
                else:
                    uf.union(node1, node2)

        if conflict < 0:
            return [edges[cycle][0], edges[cycle][1]]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return [conflictEdge[0], conflictEdge[1]]

edge = [[1,2], [2,3], [3,4], [4,1], [1,5]]
s = Solution()
print(s.findRedundantDirectedConnection(edge))