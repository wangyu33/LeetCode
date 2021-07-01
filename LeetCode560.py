#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode560.py
# Author: WangYu
# Date  : 2021/6/28

from typing import List
import bisect
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        suf = [nums[0]]
        for i in range(1,len(nums)):
            suf.append(suf[-1]+nums[i])
        ans = 0
        for i in range(len(suf)):
            target = suf[i] - k
            if target < 0:
                continue
            elif target == 0:
                ans += 1
            else:
                index = bisect.bisect_left(suf[:i],target)
                if index < i and suf[index] == target:
                    ans+=1
        return ans

nums = [-1,-1,1]
k = 0
s = Solution()
print(s.subarraySum(nums,k))