#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode334.py
# Author: WangYu
# Date  : 2020-10-08

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]