#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1856.py
# Author: WangYu
# Date  : 2021/5/10

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # 左右添加两个哨兵，方便单调栈内的判断
        nums = [0] + nums + [0]
        # 前缀和
        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)

        # 右边第一个比它小的元素下标
        right_first_smaller = [None] * len(nums)
        stack = []
        for i in range(len(nums)):
            # 如果当前元素比栈顶元素小，弹栈
            while stack and nums[i] < nums[stack[-1]]:
                right_first_smaller[stack.pop()] = i
            stack.append(i)

        # 左边第一个比它小的元素下标
        left_first_smaller = [None] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            # 如果当前元素比栈顶元素小，弹栈
            while stack and nums[i] < nums[stack[-1]]:
                left_first_smaller[stack.pop()] = i
            stack.append(i)

        # 打擂台得到答案
        res = 0
        for i in range(1, len(nums) - 1):
            left = left_first_smaller[i]
            right = right_first_smaller[i]
            res = max(res, nums[i] * (presum[right] - presum[left + 1]))
        return res % (10 ** 9 + 7)



s = Solution()
nums = [2,3,3,1,2]
print(s.maxSumMinProduct(nums))