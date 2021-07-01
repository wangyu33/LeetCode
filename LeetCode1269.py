#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1269.py
# Author: WangYu
# Date  : 2021/5/13

import functools
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.lru_cache(None)
        def dfs(pos,c):
            if c==steps and pos == 0:
                return 1
            if c==steps and pos!=0:
                return 0
            if pos > steps - c:
                return 0
            res = 0
            if pos==0:
                for i in [0,1]:
                    res+=dfs(pos+i,c+1)
            elif pos == arrLen-1:
                for i in [0,-1]:
                    res+=dfs(pos+i,c+1)
            else:
                for i in [-1,0,1]:
                    res+=dfs(pos+i,c+1)
            return res
        ans = dfs(0,0)%(10**9 + 7)
        dfs.cache_clear()
        return ans

steps = 3
arrLen = 2
s = Solution()
print(s.numWays(steps,arrLen))