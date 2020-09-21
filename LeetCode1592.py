#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1592.py
# Author: WangYu
# Date  : 2020-09-21

class Solution:
    def reorderSpaces(self, text: str) -> str:
        temp = text.strip().split()
        l = len(text) - len(''.join(temp))
        if len(temp) == 1:
            return temp[0] + ' ' * l
        l2 = l // (len(temp) - 1)
        ans = temp[0]
        for i in range(1, len(temp)):
            ans += ' ' * l2
            ans += temp[i]
            if i == len(temp) - 1:
                ans += ' ' * (l % (len(temp) - 1))
        return ans
