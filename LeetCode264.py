#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode264.py
# Author: WangYu
# Date  : 2021/4/11

from collections import defaultdict
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d = defaultdict(int)
        ret = [1]
        tmp = ret
        while len(ret) < 2000:
            tmp1 = []
            for i in tmp:
                if d[i*2] == 0:
                    tmp1.append(i*2)
                    d[i*2]=1
                if d[i*3] == 0:
                    tmp1.append(i*3)
                    d[i*3]=1
                if d[i*5] == 0:
                    tmp1.append(i*5)
                    d[i*5]=1
            ret.extend(tmp1)
            tmp = tmp1
        ret = sorted(ret)
        return ret[n-1]

n = 15
s = Solution()
print(s.nthUglyNumber(n))