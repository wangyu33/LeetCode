#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode115.py
# Author: WangYu
# Date  : 2021/3/17

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0]*m for _ in range(n)]
        cnt = 0
        for k in range(n):
            if s[k] == t[0]:
                cnt += 1
            dp[k][0] = cnt
        for i in range(1, m):
            for j in range(i,n):
                if s[j] == t[i]:
                    dp[j][i] =  max(dp[j-1][i] + dp[j-1][i-1],dp[j][i])
                else:
                    dp[j][i] = max(dp[j-1][i],dp[j][i])
        return dp[-1][-1]

s1 = "babgbag"
from queue import PriorityQueue
t = "bag"
s = Solution()
print(s.numDistinct(s1,t))