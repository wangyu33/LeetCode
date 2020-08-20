#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode45.py
# Author: WangYu
# Date  : 2020-08-14

'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
'''
class Solution:
    def jump(self, nums) -> int:
        if len(nums) <= 2:
            return 1
        end = 0
        bound = 0
        step = 0
        for index in range(len(nums) - 1):
            bound = max(index + nums[index], bound)
            if index == end:
                step = step + 1
                end = bound
        return step

nums = [2,3,1,1,4]
solution = Solution()
print(solution.jump(nums))


