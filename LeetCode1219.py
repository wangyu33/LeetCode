#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1219.py
# Author: WangYu
# Date  : 2021/3/30

from copy import deepcopy
from typing import List
from queue import PriorityQueue
from collections import defaultdict
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        def judge(state):
            ret = []
            summ,i,j,m = state
            if i-1>=0 and m[i-1][j] !=0:
                tmp = deepcopy(m)
                tmp[i-1][j] = 0
                if d[tmp] ==0:
                    d[tmp] = 1
                    ret.append((summ + m[i-1][j],i-1,j,tmp))
            if j-1>=0 and m[i][j-1] !=0:
                tmp = deepcopy(m)
                tmp[i][j-1] = 0
                if d[tmp] ==0:
                    d[tmp] = 1
                    ret.append((summ + m[i][j-1],i,j-1,tmp))
            if j+1<len(m[0]) and m[i][j+1] !=0:
                tmp = deepcopy(m)
                tmp[i][j+1] = 0
                if d[tmp] ==0:
                    d[tmp] = 1
                    ret.append((summ + m[i][j+1],i,j+1,tmp))
            if i+1<len(m) and m[i+1][j] !=0:
                tmp = deepcopy(m)
                tmp[i+1][j] = 0
                if d[tmp] ==0:
                    d[tmp] = 1
                    ret.append((summ + m[i+1][j],i+1,j,tmp))
            return ret
        maxn = 0
        ret = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    tmp = deepcopy(grid)
                    tmp[i][j] = 0
                    if d[tmp] == 0:
                        d[tmp] = 1
                        ret.append((grid[i][j],i,j,tmp))
        while ret:
            top = ret[0]
            ret.pop(0)
            ans = judge(top)
            if len(ans) == 0:
                maxn = max(maxn, top[0])
            else:
                ret.extend(ans)
        return maxn

grid = [[5,3,36,26,27],[11,31,23,30,4],[5,7,21,38,10],[39,30,10,17,13],[16,0,0,26,1],[25,0,10,0,0]]
s =Solution()
print(s.getMaximumGold(grid))