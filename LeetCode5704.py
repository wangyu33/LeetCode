#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5704.py
# Author: WangYu
# Date  : 2021/3/15

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        d = [nums[k]]
        d = set(d)
        for i in range(k-1,-1,-1):
            nums[i] = min(nums[i],nums[i+1])
            d.add(nums[i])
        for i in range(k+1,len(nums)):
            nums[i] = min(nums[i],nums[i-1])
            d.add(nums[i])
        ans = 0
        d = list(d)
        d = sorted(d,reverse=True)
        l = k
        r = k
        for key in d:
            while l-1>=0 and key <= nums[l-1]:
                l -= 1
            while r+1 < len(nums) and key <= nums[r+1]:
                r += 1
            ans = max(ans, (r-l+1)*key)
        return ans


s = Solution()
nums = [6569,9667,3148,7698,1622,2194,793,9041,1670,1872]
k = 5
print(s.maximumScore(nums,k))