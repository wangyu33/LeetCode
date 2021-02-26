#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1766.py
# Author: WangYu
# Date  : 2021/2/24

import collections
from typing import *
import math

class Solution:
    def getCoprimes(self, nums: List[int], e: List[List[int]]) -> List[int]:
        n = len(nums)
        edges = collections.defaultdict(list)
        for x, y in e:
            edges[x].append(y)
            edges[y].append(x)

        coprime = collections.defaultdict(list)
        for i in range(1, 50 + 1):
            for j in range(1, 50 + 1):
                if math.gcd(i, j) == 1:
                    coprime[i].append(j)

        pos = [-1] * 51
        ans = [-1] * n
        stk = []

        def dfs(u, fa):
            dep = -1
            for p in coprime[nums[u]]:
                dep = max(dep, pos[p])
            ans[u] = (-1 if dep == -1 else stk[dep])

            tmp = pos[nums[u]]
            pos[nums[u]] = len(stk)
            stk.append(u)

            for v in edges[u]:
                if v != fa:
                    dfs(v, u)

            pos[nums[u]] = tmp
            stk.pop()

        dfs(0, -1)
        return ans

nums = [2,3,3,2]
edges = [[0,1],[1,2],[1,3]]
s = Solution()
print(s.getCoprimes(nums,edges))
