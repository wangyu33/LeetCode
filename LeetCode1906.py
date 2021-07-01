#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1906.py
# Author: WangYu
# Date  : 2021/6/21

from typing import List
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 差分数组
        diff = [[0] * 101]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l,r in queries:
            res = 100 # 最大不会超过100
            last = -100
            # 我们通过差分数组求得l到r之间有哪些数
            for i in range(1, 101):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < 100 else -1)
        return ans

nums = [4,5,2,2,7,10]
queries = [[2,3],[0,2],[0,5],[3,5]]
s = Solution()
print(s.minDifference(nums,queries))