#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode279.py
# Author: WangYu
# Date  : 2021/6/11

from collections import defaultdict
class Solution:
    def numSquares(self, n: int) -> int:
        table = []
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(1, 101):
            table.append(i * i)
            dp[i*i] = 1

        for i in range(1, n + 1):
            if dp[i] != 0:
                continue
            for j in table:
                if j >= i:
                    break
                if dp[i] == 0:
                    dp[i] = dp[i - j] + 1
                else:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[n]

n = 13
s = Solution()
print(s.numSquares(n))