#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1695.py
# Author: WangYu
# Date  : 2021/4/1

from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        window = set()              #滑动窗口
        win_sum = 0                 #窗口内元素和
        L = 0
        for R in range(n):
            while window and nums[R] in window: #右移左指针L
                window.remove(nums[L])
                win_sum -= nums[L]
                L += 1
            window.add(nums[R])         #加入窗口
            win_sum += nums[R]          #做好统计
            res = max(res, win_sum)     #维持 更新
        return res

a = [4,2,4,5,6]
s = Solution()
print(s.maximumUniqueSubarray(a))