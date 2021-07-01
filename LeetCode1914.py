#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1914.py
# Author: WangYu
# Date  : 2021/6/28

from typing import List
from copy import deepcopy
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def gao(g):
            ans = deepcopy(g)
            nrow = len(g)
            ncol = len(g[0])
            x = 0
            y = 0
            while x<ncol//2 and y < nrow//2:
                for i in range(x,ncol-1-x):
                    print(x,i)
                    ans[x][i] = g[x][i+1]
                for i in range(nrow-1-y,y,-1):
                    print(i, y)
                    ans[i][y] = g[i-1][y]
                for i in range(ncol-1-x,x,-1):
                    print(nrow-1-y, i)
                    ans[nrow-1-y][i] = g[nrow-1-y][i-1]
                for i in range(y,nrow-1-y):
                    print(i,ncol-1-x)
                    ans[i][ncol-1-x] = g[i+1][ncol-1-x]
                x+=1
                y+=1
            return ans
        for i in range(k):
            grid = gao(grid)
        return grid

grid = [[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]]
k = 1
s = Solution()
print(s.rotateGrid(grid,k))