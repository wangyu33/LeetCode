#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode399.py
# Author: WangYu
# Date  : 2021/1/20
from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(list)
        key = []
        for i in equations:
            for j in i:
                if j not in key:
                    key.append(j)
                    d[j].extend([j, 1.0])
        # fa = {i:i for i in key}
        def find(a):
            if a != d[a][0]:
                d[a][0] = find(d[a][0])
                d[a][1] = d[a][1] * d[d[a][0]][1]

            base = 1
            fa = a
            while d[fa][0] != a:
                fa = d[a][0]
                base *= d[fa][1]

            while a != fa:
                original_father = d[a][0]
                ##### 离根节点越远，放大的倍数越高
                d[a][1] *= base
                base /= d[original_father][1]
                #####
                d[a][0] = fa
                a = original_father

            return root

            return d[a][0]

        def union(a,b, value):
            fa = find(a)
            fb = find(b)
            if fa != fb:
                d[fa][0] = fb
                d[fa][1] = d[b][1] * value / d[a][1]


        for i in range(len(equations)):
            if find(equations[i][0]) != find(equations[i][1]):
                union(equations[i][0], equations[i][1], values[i])
        ans = []
        for a,b in queries:
            if a not in d or b not in d:
                ans.append(-1.0)
            else:
                find(a)
                find(b)
                ans.append(d[a][1]/d[b][1])
        return ans


equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
s = Solution()
print(s.calcEquation(equations,values,queries))