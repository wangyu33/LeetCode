#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5507.py
# Author: WangYu
# Date  : 2020-09-06

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for index, ch in enumerate(s):
            if ch == '?':
                for a in "abc":
                    yes = 1
                    if (index > 0 and a == s[index - 1]):
                        yes = 0
                    if (index < len(s) - 1 and a == s[index + 1]):
                        yes = 0
                    if (yes == 1):
                        s[index] = a
                        break
        return ''.join(s)
s = Solution()
str1 = "?zs"
print(s.modifyString(str1))