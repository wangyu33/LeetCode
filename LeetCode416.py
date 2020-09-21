#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode416.py
# Author: WangYu
# Date  : 2020-09-21
import functools
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        nums_sum = sum(nums)
        dp = [[0] * (nums_sum) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = 1

        for i in range(1, len(nums) + 1):
            for j in range(1, nums_sum):
                if nums[i - 1] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
        if dp[len(nums)][nums_sum // 2]:
            return True
        return False

s = Solution()
print(s.canPartition([1, 2, 5]))
