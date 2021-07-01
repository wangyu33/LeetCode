#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1862.py
# Author: WangYu
# Date  : 2021/5/17

from typing import List

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        n = max(nums)
        import collections
        # 对元素进行技术
        cnt = collections.Counter(nums)
        # 动态规划
        memo = [0]*(n+1)
        # 筛法
        for num in cnt:
            for i in range(1, 1+n//num):
                memo[i*num] += 1 * cnt[num]
        for i in range(1,len(memo)):
            memo[i] += memo[i-1]
        ans=0
        # 所有结果之和
        for num in nums:
            ans += memo[num]
            ans = ans % (10**9+7)
        return ans

nums = [2,5,9]
s = Solution()
print(s.sumOfFlooredPairs(nums))