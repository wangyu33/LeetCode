#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LCS3.py
# Author: WangYu
# Date  : 2021/6/21
from typing import List
class Solution:
    def largestArea(self, grid: List[str]) -> int:

        def dfs(grid, r, c, sig):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return -1
            if grid[r][c] == '0':
                return -1
            if grid[r][c] != sig:
                return 0

            grid[r][c] = '-1'

            a1 = dfs(grid, r - 1, c, sig)
            a2 = dfs(grid, r + 1, c, sig)
            a3 = dfs(grid, r, c - 1, sig)
            a4 = dfs(grid, r, c + 1, sig)

            if a1 != -1 and a2 != -1 and a3 != -1 and a4 != -1:
                return 1 + a1 + a2 + a3 + a4
            else:
                return -1

        grid = [list(grid[idx]) for idx in range(len(grid))]

        ans = 0
        nrow, ncol = len(grid), len(grid[0])
        for irow in range(nrow):
            for icol in range(ncol):
                if grid[irow][icol] != '0' and grid[irow][icol] != '-1':
                    ans = max(dfs(grid, irow, icol, grid[irow][icol]), ans)
        return ans

grid = ["11111100000","21243101111","21224101221","11111101111"]
s=Solution()
print(s.largestArea(grid))