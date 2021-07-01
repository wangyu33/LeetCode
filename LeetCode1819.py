#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1819.py
# Author: WangYu
# Date  : 2021/4/5

from typing import List
import math
# class Solution:
#     def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
#         ret = set(nums)
#         tmp = list(ret)
#         def dfs(idx, g, L):
#
#             if g == 1:
#                 if g in ret:
#                     return
#                 else:
#                     ret.add(g)
#                     return
#             elif g!= -1:
#                 if g not in ret:
#                     ret.add(g)
#             if idx >= len(tmp)-1:
#                 return
#             if len(L) == 0:
#                 dfs(idx+1, tmp[idx+1], [tmp[idx+1]])
#                 dfs(idx+1,g, L)
#             else:
#                 dfs(idx+1, math.gcd(g,tmp[idx+1]),L+[tmp[idx+1]])
#                 dfs(idx+1, g, L)
#         dfs(-1,-1,[])
#         return len(ret)
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        f = [0 for k in range(200010)]
        ans = 0
        for num in nums:
            if f[num] == 0:
                f[num] += 1
                ans += 1
        maxn = max(nums)
        for i in range(1, maxn + 1):
            if f[i]: continue
            r = 0
            for j in range(i, maxn + 1, i):
                if f[j]:
                    r = math.gcd(r, j)
                    if r == i:
                        ans += 1
                        break
        return ans

nums = [6,10,3]
s = Solution()
print(s.countDifferentSubsequenceGCDs(nums))