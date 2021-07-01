#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1371.py
# Author: WangYu
# Date  : 2021/6/28


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        Y = ['a','e','i','o','u']
        d = {0:0}
        cur = 0
        maxn = 0
        for i in range(len(s)):
            # tmp = s[i]
            if s[i] in Y:
                cur ^= 1<<(ord(s[i])-ord('a')+1)
            if cur < 2:
                maxn = max(maxn,i+1)
            else:
                if cur in d:
                    maxn = max(maxn, i-d[cur])
                else:
                    d[cur] = i
        return maxn


t = "eleetminicoworoep"
s = Solution()
print(s.findTheLongestSubstring(t))