#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode657.py
# Author: WangYu
# Date  : 2020-08-28

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves == '':
            return True

        index = [0,0]
        for s in moves:
            if s == 'U':
                index[0] = index[0] + 1
            if s == 'D':
                index[0] = index[0] - 1
            if s == 'L':
                index[1] = index[1] + 1
            if s == 'R':
                index[1] = index[1] - 1
        if index[0] == 0 and index[1] == 0:
            return True
        return False

s = Solution()
t = 'UD'
s.judgeCircle(t)
