#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode70.py
# Author: WangYu
# Date  : 2020-09-08

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        import copy
        def dfs(n,k,start, temp):
            if len(temp) == k:
                a = copy.deepcopy(temp)
                ans.append(a)
                return
            for i in range(start, n + 1):
                temp.append(i)
                dfs(n, k, i + 1, temp)
                temp.pop()
        dfs(n,k,1,[])
        return ans
n = 4
k = 2
s = Solution()
print(s.combine(n,k))


