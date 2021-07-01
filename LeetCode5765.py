#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5765.py
# Author: WangYu
# Date  : 2021/5/24

from collections import defaultdict
import re
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        d = defaultdict(int)
        L = [0]
        d[0] = 1
        if len(max(re.split('0+', s), key=len)) >= maxJump:
            return False
        while L:
            tmp = []
            for i in L:
                for j in range(minJump,maxJump+1):
                    if i+j < len(s) and s[i+j] == '0' and d[i+1] == 0:
                        tmp.append(i+j)
                        d[i+j] = 1
            if d[len(s)-1] == 1:
                return True
            L = tmp
        return d[len(s)-1] == 1
s = Solution()
ss = "011010"
minJump = 2
maxJump = 3
print(s.canReach(ss,minJump,maxJump))