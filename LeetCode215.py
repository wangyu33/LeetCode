#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode215.py
# Author: WangYu
# Date  : 2021/3/15

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        ans = nums[:k]
        heapq.heapify(ans)
        for i in nums[k:]:
            heapq.heappushpop(ans,i)
        return ans[0]
nums = [7,2,9,1,2,4,5,5,6]
k= 4
s = Solution()
print(s.findKthLargest(nums,k))