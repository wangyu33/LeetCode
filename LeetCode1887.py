#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1887.py
# Author: WangYu
# Date  : 2021/6/10

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        nums = list(set(nums))
        nums = sorted(nums, reverse = True)
        ans = 0
        for i in range(len(nums[:-1])):
            d[nums[i+1]] += d[nums[i]]
            ans += d[nums[i]]
        return ans

nums = [7,9,10,8,6,4,1,5,2,3]
s = Solution()
print(s.reductionOperations(nums))
