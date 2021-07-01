#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode81.py
# Author: WangYu
# Date  : 2021/4/7

import bisect
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in nums:
        #     return True
        # return False
        if nums[0] < nums[-1]:
            return nums[bisect.bisect_left(nums, target)] == target
        l = 0
        r = len(nums) - 1
        while r > l and nums[r] == nums[0]:
            r -= 1
        while l < r:
            mid = (l +r) // 2
            if nums[mid] >= nums[0]:
                l = mid+1
            else:
                r = mid
        # while l-1>=0 and nums[l] >= nums[l - 1]:
        #     l += 1
        if target >= nums[0]:
            index = bisect.bisect_left(nums[:l], target)
        else:
            index = l + bisect.bisect_left(nums[l:], target)
        return nums[index] == target

nums = [3,1]
target = 3
s = Solution()
print(s.search(nums,target))