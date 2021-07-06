#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5803.py
# Author: WangYu
# Date  : 2021/7/5

from typing import List
import random


class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        l,r = 1, len(min(paths, key=lambda p: len(p)))
        mod = 10000000079
        base = 1000007
        ans = 0
        while l <= r:
            mid = (l+r)//2
            s = set()
            tmp = pow(base,mid, mod)
            flag = 1
            for i in range(len(paths)):
                cur = 0
                t = set()
                for j in range(mid):
                    cur = (cur*base+paths[i][j])%mod
                t.add(cur)
                for j in range(mid,len(paths[i])):
                    cur = (cur*base+paths[i][j]-paths[i][j-mid]*tmp)%mod
                    t.add(cur)
                if i == 0:
                    s = t
                else:
                    s = s&t
                if len(s)==0:
                    flag = 0
                    break
            if flag == 0:
                r = mid-1
            else:
                l = mid+1
                ans = mid
        return ans



n = 5

paths = [[1,2,3,4],[4,1,2,3],[4]]
s = Solution()
print(s.longestCommonSubpath(n,paths))