#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File    : LeetCode1617.py
# Author  : WangYu
# Date    : 2021/3/9

from typing import List
from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        node = defaultdict(list)
        idx = defaultdict(list)
        for a,b in edges:
            node[a].append(b)
            node[b].append(a)
        for i in range(1,n+1):
            idx[i] = [0] * 16
        for k in range(1,n+1):
            tmp = [k]
            flag = set(tmp)
            cnt = 1
            while len(tmp) > 0:
                tmp2 = []
                for i in tmp:
                    for j in node[i]:
                        if j not in flag:
                            tmp2.append(j)
                            flag.add(j)
                            idx[k][cnt]+=1
                tmp = tmp2
                cnt += 1
        ret = []
        for i in range(1,n+1):
            print(i,idx[i])
        for i in range(1,n):
            summ = 0
            for j in range(1,n+1):
                summ+= idx[j][i]
            ret.append(summ)
        return ret

n = 4
edges = [[1, 2], [2, 3], [2, 4]]
s = Solution()
print(s.countSubgraphsForEachDiameter(n,edges))