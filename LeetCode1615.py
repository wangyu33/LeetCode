#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1615.py
# Author: WangYu
# Date  : 2020-10-12
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mat = [0] * n
        for r  in roads:
            mat[r[0]] += 1
            mat[r[1]] += 1
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if [i,j] in roads or [j,i] in roads:
                    ans = max(ans, mat[i] + mat[j] -1)
                else:
                    ans = max(ans, mat[i] + mat[j])
        return ans