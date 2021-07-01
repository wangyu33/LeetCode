#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode525.py
# Author: WangYu
# Date  : 2021/6/3

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # 前缀和字典: key为1的数量和0的数量的差值,value为对应坐标
        hashmap = {0:-1}
        # 当前1的数量和0的数量的差值
        counter = ans = 0
        for i,num in enumerate(nums):
            # 每多一个1，差值+1
            if num:
                counter += 1
            # 每多一个0，差值-1
            else:
                counter -= 1
            # 如果存在1和0的数量差值相等的地方，那么说明后者到前者之前1和0的数量相等！
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans

s = Solution()
num = [0,1,0,1]
print(s.findMaxLength(num))