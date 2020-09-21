#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1594.py
# Author: WangYu
# Date  : 2020-09-21

from typing import List
#dfs剪枝超时
# class Solution:
#     def maxProductPath(self, grid: List[List[int]]) -> int:
#         val = grid[0][0]
#         self.row = len(grid)
#         self.col = len(grid[0])
#         self.ans = -1
#         def dfs(r,c, temp):
#             if temp == 0:
#                 self.ans = max(self.ans, 0)
#                 return
#             if r == self.row - 1 and c == self.col - 1:
#                 self.ans = max(self.ans, temp)
#                 #print(self.ans)
#                 return
#             if r + 1 <= self.row - 1:
#                 dfs(r + 1, c, temp * grid[r + 1][c])
#             if c + 1 <= self.col - 1:
#                 dfs(r, c + 1, temp * grid[r ][c + 1])
#         dfs(0,0, grid[0][0])
#         if self.ans < 0:
#             return -1
#         else:
#             return self.ans % (10 ** 9 + 7)
#


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.row = len(grid)
        self.col = len(grid[0])
        dp1 = [[0] * self.col for _ in range(self.row)]
        dp2 = [[0] * self.col for _ in range(self.row)]

        dp1[0][0] = dp2[0][0] = grid[0][0]
        for i in range(1, self.col):
            dp1[0][i] = dp2[0][i] = dp1[0][i-1] * grid[0][i]

        for i in range(1, self.row):
            dp1[i][0] = dp2[i][0] = dp1[i-1][0] * grid[i][0]

        for i in range(1, self.row):
            for j in range(1, self.col):
                if grid[i][j] == 0:
                    dp1[i][j] = dp2[i][j] = 0
                dp1[i][j] = max(dp1[i-1][j] * grid[i][j],dp1[i][j-1]* grid[i][j],
                                    dp2[i-1][j] * grid[i][j],dp2[i][j-1]* grid[i][j])
                dp2[i][j] = min(dp1[i - 1][j] * grid[i][j], dp1[i][j - 1] * grid[i][j],
                                dp2[i - 1][j] * grid[i][j], dp2[i][j - 1] * grid[i][j])
        ans = dp1[-1][-1]
        if ans < 0:
            return -1
        return int(ans % (10**9 + 7))

grid = [[1,4,4,0],[-2,0,0,1],[1,-1,1,1]]
s = Solution()
print(s.maxProductPath(grid))