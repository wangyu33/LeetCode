#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode518.py
# Author: WangYu
# Date  : 2020-09-21

from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount < min(coins):
            return 0
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount + 1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
amount = 5
coins = [1,2,5]
s = Solution()
print(s.change(amount,coins))