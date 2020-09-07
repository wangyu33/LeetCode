#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5510.py
# Author: WangYu
# Date  : 2020-09-06

from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 分别求出Alice与Bob分别遍历下的并查集,若集合数量大于1则返回-1;否则求出type3下的并查集,对于type3并查集下的每个闭包,其内部至少需要元素数量 - 1条边;
        # 对于两个闭包之间,至少需要type1,type2两条边才能使得两人都能完全遍历,总边数 - 剩余最小边数即为所求
        Aliceuf,Bobuf,type3uf = UnionFind(n),UnionFind(n),UnionFind(n)
        cnt = 0
        for i in range(len(edges)):
            if edges[i][0] == 3:
                if not type3uf.union(edges[i][1] - 1,edges[i][2] - 1):
                    cnt += 1
        tmp_cnt = cnt
        import copy
        Aliceuf = copy.deepcopy(type3uf)
        Bobuf = copy.deepcopy(type3uf)
        Alic_cnt = 0
        for i in range(len(edges)):
            if edges[i][0] == 1:
                if not Aliceuf.union(edges[i][1] - 1,edges[i][2] - 1):
                    cnt += 1
                    Alic_cnt += 1
        Bobuf_cnt = 0
        for i in range(len(edges)):
            if edges[i][0] == 2:
                if not Bobuf.union(edges[i][1] - 1,edges[i][2] - 1):
                    cnt += 1
                    Bobuf_cnt += 1
        if tmp_cnt + Alic_cnt < n-1 or tmp_cnt + Bobuf_cnt < n-1:
            return -1
        else:
            return len(edges) - cnt

# 并查集
class UnionFind():
    def __init__(self, n):
        self.uf = [-1] * n
        self.count_= n

    def find(self, x):
        r = x
        while self.uf[x] >= 0:
            x = self.uf[x]
        # 路径压缩
        while r != x:
            self.uf[r],r = x,self.uf[r]
        return x

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        if ux == uy:
            return True
        # 规模小的优先合并
        if self.uf[ux] < self.uf[uy]:
           self.uf[ux] += self.uf[uy]
           self.uf[uy] = ux
        else:
           self.uf[uy] += self.uf[ux]
           self.uf[ux] = uy
        self.count_ -= 1
        return False

    def count(self):
        return self.count_

s = Solution()
n, edge = 4,[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(s.maxNumEdgesToRemove(n, edge))

