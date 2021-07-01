#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode982.py
# Author: WangYu
# Date  : 2021/3/30

from typing import List
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        mem = [0] * 65536
        mask = (1 << 16) - 1
        # 标记数字能够令哪些数字相与变成0，也就是遍历所有的0所在的位置组成的数字
        for num in A:
            mk = mask ^ num
            i = mk
            while i:
                mem[i] += 1
                # 这一步是关键，位运算找出所有的满足条件的数字
                i = (i - 1) & mk
            # 数字0肯定能够相与变成0
            mem[0] += 1
        res = 0
        for n1 in A:
            for n2 in A:
                res += mem[n1 & n2]
        return res

s = Solution()
a = [2,1,3]
print(s.countTriplets(a))