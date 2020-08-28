#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode495.py
# Author: WangYu
# Date  : 2020-08-25

'''
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
'''

from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return []
        ans = [[nums[0]]]
        for num in nums[1:]:
            temp = ans.copy()
            for num_list in ans:
                if num >= num_list[-1]:
                    a = num_list.copy()
                    a.append(num)
                    temp.append(a)
            temp.append([num])
            ans = temp
            # ans.append([num])
        temp = []
        for a in ans:
            if len(a) >= 2 and a not in temp:
                temp.append(a)
        print(temp)
        return temp

s = Solution()
nums = [4, 6, 7, 7]
s.findSubsequences(nums)