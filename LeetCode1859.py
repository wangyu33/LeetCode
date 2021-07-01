#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1859.py
# Author: WangYu
# Date  : 2021/5/17

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = [''] * len(s)
        for i in range(len(s)):
            index = int(s[i][-1])
            l = len(s[i])
            tmp = s[i][:l-1]
            ans[index-1] = tmp
        return ''.join(ans)

s = "is2 sentence4 This1 a3"
s1 = Solution()
print(s1.sortSentence(s))