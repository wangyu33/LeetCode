#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode347.py
# Author: WangYu
# Date  : 2020-09-07

from typing import List
from collections import  defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        for i in nums:
            dict[i] = dict[i] + 1
        ans = []
        for i,num in enumerate(sorted(dict.items(),key = lambda kv:(kv[1], kv[0]),reverse=True)):
            if i < k:
                ans.append(num[0])
            else:
                break
        return ans


S = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
print(S.topKFrequent(nums, k))
