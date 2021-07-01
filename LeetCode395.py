#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode395.py
# Author: WangYu
# Date  : 2021/3/30

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

s = "aaabb"
k = 3
ss = Solution()
print(ss.longestSubstring(s,k))