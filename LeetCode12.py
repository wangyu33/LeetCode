#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode12.py
# Author: WangYu
# Date  : 2021/5/14

from collections import defaultdict
class Solution:
    def intToRoman(self, nums: int) -> str:
        d = defaultdict(int)
        table = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CD']
        num = [1,5,10,50,100,500,1000,4,9,40,90,400,900]
        for i in range(len(table)):
            d[table[i]] = num[i]
        d = sorted(d.items(), key = lambda x:x[1], reverse = True)

        ans = ''
        for key,val in d:
            ans += (key*(nums//val))
            nums = nums - val * (nums//val)
        return ans

num = 58
s = Solution()
print(s.intToRoman(num))
