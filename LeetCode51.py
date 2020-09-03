#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode51.py
# Author: WangYu
# Date  : 2020-09-03

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chess = [['.'] * (n + 1) for _ in range(n + 1)]
        ans = []
        col_flag = [0] * (n + 1)

        def judge(row, col):
            for i in range(1, row):
                for j in range(1, n + 1):
                    if chess[i][j] == 'Q' and abs(i - row) == abs(j - col):
                        return False
            return True

        def dfs(row, col):
            if row == n and judge(row, col):
                temp = [''.join(i[1:]) for i in chess[1:]]
                ans.append(temp)
            r = row + 1
            for c in range(1, n +1 ):
                if col_flag[c] == 0 and judge(r, c):
                    chess[r][c] = 'Q'
                    col_flag[c] = 1
                    dfs(r, c)
                    chess[r][c] = '.'
                    col_flag[c] = 0

        for i in range(1, n + 1):
            chess[1][i] = 'Q'
            col_flag[i] = 1
            dfs(1, i)
            chess[1][i] = '.'
            col_flag[i] = 0
        return ans

num = 4
s = Solution()
from pprint import pprint
pprint(s.solveNQueens(num))

