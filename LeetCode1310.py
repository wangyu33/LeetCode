#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1310.py
# Author: WangYu
# Date  : 2021/5/12

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(arr), len(queries)
        c = [0] * 100009

        def lowbit(x):
            tmp = x & -x
            return x & -x

        def add(x, u):
            i = x
            while i <= n:
                c[i] ^= u
                i += lowbit(i)

        def query(x):
            ans = 0
            i = x
            while i:
                ans ^= c[i]
                i -= lowbit(i)
            return ans

        for i in range(1, n + 1):
            add(i, arr[i - 1])

        ans = [0] * m
        for i in range(m):
            ans[i] = query(queries[i][1] + 1) ^ query(queries[i][0])
        return ans

s = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(s.xorQueries(arr,queries))