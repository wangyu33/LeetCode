#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1542.py
# Author: WangYu
# Date  : 2021/6/28

class Solution:
    def longestAwesome(self, s: str) -> int:
        d = {}
        cur = 0
        maxn = 0
        L = [1<<(i+1) for i in range(10)]
        for i in range(len(s)):
            cur ^= 1<<(int(s[i])+1)
            if cur == 0:
                maxn = max(maxn,i+1)
            elif cur in L:
                maxn = max(maxn,i+1)
            else:
                for k in L:
                    tmp = cur^k
                    if cur^k in d:
                        maxn = max(maxn, i - d[cur^k])
            if cur not in d:
                d[cur] = i
        return maxn

s = "3242415"
t = Solution()
print(t.longestAwesome(s))