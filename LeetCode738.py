#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode738.py
# Author: WangYu
# Date  : 2020/12/15

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        num = list(str(N))
        for i in range(len(num) - 1, 0, -1):
            if num[i] == '0':
                temp = int(''.join(num[i:]))
                return self.monotoneIncreasingDigits(int(''.join(num))-int(''.join(num[i:]))-1)
            if int(num[i]) < int(num[i - 1]):
                return self.monotoneIncreasingDigits(int(''.join(num)) - int(''.join(num[i:])) - 1)

        return int(''.join(num))

s = 989998
a = Solution()
print(a.monotoneIncreasingDigits(s))