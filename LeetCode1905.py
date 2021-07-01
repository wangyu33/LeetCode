#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1905.py
# Author: WangYu
# Date  : 2021/6/21

from typing import List
from collections import defaultdict
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        flag = defaultdict(int)
        nrow = len(grid2)
        ncol = len(grid2[0])
        cnt = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid2[i][j] == 0 or flag[(i, j)] == 1:
                    continue

                t = [(i, j)]
                node_flag = 1
                while len(t) > 0:
                    a, b = t.pop()
                    flag[(a,b)] = 1
                    if grid1[a][b] != 1:
                        node_flag = 0
                    if a - 1 >= 0 and grid2[a - 1][b] == 1 and flag[(a-1,b)] == 0:
                        t.append((a - 1, b))
                    if a + 1 <= nrow - 1 and grid2[a + 1][b] == 1 and flag[(a+1,b)] == 0:
                        t.append((a + 1, b))
                    if b - 1 >= 0 and grid2[a][b - 1] == 1 and flag[(a,b-1)] == 0:
                        t.append((a, b - 1))
                    if b + 1 <= ncol - 1 and grid2[a][b + 1] == 1 and flag[(a,b+1)] == 0:
                        t.append((a, b + 1))
                if node_flag:
                    cnt += 1
        return cnt

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
s = Solution()
print(s.countSubIslands(grid1,grid2))

