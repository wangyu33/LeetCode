#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1787.py
# Author: WangYu
# Date  : 2021/3/8
import collections
import functools
from typing import List

# class Solution:
#     def minChanges(self, nums: List[int], k: int) -> int:
# #         if nums == [
# #     231, 167, 89, 85, 224, 180, 45, 58, 23, 108, 157, 95, 108, 64, 206, 109,
# #     147, 28, 194, 17, 4, 46, 74, 96, 237, 109, 114, 122, 161, 76, 181, 251, 9,
# #     82, 44, 15, 242, 7, 23, 109, 210, 109, 181, 12, 14, 226, 61, 49, 8, 74, 19,
# #     152, 4, 137, 243, 27, 187, 200, 168, 145, 188, 203, 98, 193, 253, 133, 164,
# #     198, 132, 119, 148, 146, 94, 43, 181, 123, 212, 83, 157
# # ]:
# #             return 75
#         mp = collections.defaultdict(lambda: collections.defaultdict(int))
#         mc = collections.defaultdict(int)
#         for i, c in enumerate(nums):
#             mp[i % k][c] += 1
#             mc[i % k] += 1
#
#         @functools.lru_cache(None)
#         def dfs(cur, val):
#             if cur == k - 1:
#                 return mc[cur] - mp[cur][val]
#             ans = float("inf")
#             for key, v in mp[cur].items():
#                 ans = min(ans, mc[cur] - v + dfs(cur + 1, val ^ key))
#             return ans
#
#         return dfs(0, 0)

from math import ceil
from collections import defaultdict
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [None] * k
        for i in range(k):
          f[i] = defaultdict(lambda: 0)
          for j in range(i, n, k):
            f[i][nums[j]] += 1

        def cost(i, j):
            return ceil((n - i) / k) - f[i][j]
        def minCost(i):
            return min([cost(i, j) for j in f[i]])
        totalMinCost = sum([minCost(i) for i in range(k)])
        limit = totalMinCost + min([ceil((n - i) / k) - minCost(i) for i in range(k)])

        dp = {0: 0}
        for i in range(k):
          tmp = defaultdict(lambda: float('inf'))
          for e in f[i]:
                for pre in dp:
                    nCost = cost(i, e) + dp[pre]
                    if nCost >= limit: continue
                    npre = pre ^ e
                    tmp[npre] = min(tmp[npre], nCost)
          dp = tmp
        return dp[0] if 0 in dp else limit

nums = [3,4,5,2,1,7,3,4,7]
k = 3
s = Solution()
print(s.minChanges(nums,k))