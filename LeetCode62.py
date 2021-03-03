#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode62.py
# Author: WangYu
# Date  : 2021/3/2

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

m = 3
n = 7
s = Solution()
print(s.uniquePaths(m,n))