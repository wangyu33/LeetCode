#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode33.py
# Author: WangYu
# Date  : 2021/2/26

from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[-1] >= nums[0]:
            id = bisect.bisect_left(nums,target)
            if id < len(nums) and nums[id] == target:
                return id
            else:
                return -1
        if target >= nums[0]:
            l = 0
            r = len(nums)-1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > nums[0] and nums[mid] > target:
                    id = bisect.bisect_left(nums[:mid], target)
                    if id < len(nums) and nums[id] == target:
                        return id
                    else:
                        return -1
                elif nums[mid] > nums[0]:
                    l = mid + 1
                elif nums[mid] <= nums[0]:
                    r = mid
        if target < nums[0] and target <= nums[-1]:
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[0] and nums[mid] <= target:
                    id = bisect.bisect_left(nums[mid:], target)
                    if id < len(nums) and nums[mid + id] == target:
                        return id + mid
                    else:
                        return -1
                elif nums[mid] > nums[0]:
                    l = mid + 1
                elif nums[mid] <= nums[0]:
                    r = mid
        return -1

nums = [1]
target = 2
s = Solution()
print(s.search(nums,target))