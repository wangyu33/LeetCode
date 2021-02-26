#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke_1.py
# Author: WangYu
# Date  : 2021/1/21
'''
这里有一堆物资待分配，物资总数量不超过200，每件物资重量不超过100。
请问是否可以将这堆物资分配给两个队伍，使得两个队伍的全部的物资重量和相等。
'''
class Solution:
    def canPartition(self , nums):
        # write code here
        if nums == []:
            return True
        if sum(nums) % 2 == 1:
            return False
        nums.sort()
        target = int(sum(nums)//2)
        dp = [[0] * (target+1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(nums[i-1], target+1):
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i-1]])
        return dp[-1][-1] == 1


s = Solution()
a = [1,5,5,11]
print(s.canPartition(a))