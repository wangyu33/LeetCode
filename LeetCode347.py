#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode347.py
# Author: WangYu
# Date  : 2020-09-07

from typing import List
from collections import  defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #方法1    排序
        # dict = defaultdict(int)
        #
        # for i in nums:
        #     dict[i] = dict[i] + 1
        # ans = []
        # for i,num in enumerate(sorted(dict.items(),key = lambda kv:(kv[1], kv[0]),reverse=True)):
        #     if i < k:
        #         ans.append(num[0])
        #     else:
        #         break
        # return ans
        #方法2    最小堆
        dict = defaultdict(int)
        for i in nums:
            dict[i] = dict[i] + 1
        ans = []
        for key in dict:
            ans.append((dict[key],key))
        # print(ans)
        heapq.heapify(ans)
        while len(ans) > k:
            heapq.heappop(ans)
        temp = []
        for i in range(k):
            temp.append(heapq.heappop(ans)[1])
        return temp


S = Solution()
nums = [4,1,-1,2,-1,2,3]
k = 2
print(S.topKFrequent(nums, k))
