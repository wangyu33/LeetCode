#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1614.py
# Author: WangYu
# Date  : 2020-10-12

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        s = list(s)
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
                ans = max(cnt, ans)
            elif i == ')':
                cnt -= 1
        return ans