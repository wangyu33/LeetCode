#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1582.py
# Author: WangYu
# Date  : 2020-09-14

from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] != 1:
                    continue
                else:
                    sum = 0
                    sum += mat[i][j]
                    for k in range(row):
                        if k != i:
                            sum += mat[k][j]
                    for k in range(col):
                        if k != j:
                            sum += mat[i][k]
                    if sum == 1:
                        ans += 1
        return ans

mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
s = Solution()
print(s.numSpecial(mat))

