#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode54.py
# Author: WangYu
# Date  : 2021/2/26

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        flag = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ret = []
        r,c = 0,0
        tmp = 0
        while len(ret) < len(flag) * len(flag[0]):
            ret.append(matrix[r][c])
            flag[r][c] = 1
            if tmp == 0:
                if c+1 == len(flag[0]) or flag[r][c+1] == 1:
                    tmp = 1
                    r = r + 1
                else:
                    c = c + 1
            elif tmp == 1:
                if r+1 == len(flag) or flag[r+1][c] == 1:
                    tmp = 2
                    c = c - 1
                else:
                    r = r + 1
            elif tmp == 2:
                if c-1 == -1 or flag[r][c-1] == 1:
                    tmp = 3
                    r = r - 1
                else:
                    c = c - 1
            elif tmp == 3:
                if r-1 == -1 or flag[r-1][c] == 1:
                    tmp = 0
                    c = c+1
                else:
                    r = r - 1
        return ret

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.spiralOrder(matrix))
