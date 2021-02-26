#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode474.py
# Author: WangYu
# Date  : 2021/1/21
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        d1 = {}
        d0 = {}
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(len(strs) + 1)]
        for i,s in enumerate(strs):
            d0[i] = 0
            d1[i] = 0
            for j in list(s):
                if j == '1':
                    d1[i] += 1
                if j == '0':
                    d0[i] += 1
        # maxn = 0
        for i in range(1,len(strs)+1):
            for j in range(m+1):
                for k in range(n+1):
                    if j - d0[i-1] >= 0 and k - d1[i-1] >= 0:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-d0[i-1]][k-d1[i-1]] + 1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
                    # maxn = max(maxn, dp[i-1][j][k])
        return dp[-1][-1][-1]

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
s = Solution()
print(s.findMaxForm(strs,m,n))