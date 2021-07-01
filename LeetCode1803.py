#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1803.py
# Author: WangYu
# Date  : 2021/3/22

from typing import List
import collections


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # indexing = [2**i for i in range(15, -1, -1)]
        to_key = lambda t: bin(t)[2:].rjust(16, '0')

        count = collections.Counter()
        for t in nums:
            key = to_key(t)
            for i in range(16):
                count[key[:i + 1]] += 1

        # print(dict(count))

        def countm(maxv):
            to_ret = 0
            ky = to_key(maxv)
            for t in nums:
                k = to_key(t)
                # print(ky, k)
                prex = ''
                for i in range(16):
                    if ky[i] == '0':
                        prex += k[i]
                    else:
                        # print('check', prex+k[i], count[prex+k[i]])
                        tmp = prex + k[i]
                        to_ret += count[prex + k[i]]
                        prex += '1' if k[i] == '0' else '0'
                # print('to_ret', to_ret)

            # print('maxv', maxv, to_ret)
            return to_ret

        # return countm(high+1)
        # return countm(low)
        return (countm(high + 1) - countm(low)) // 2

nums = [1,4,2,7]
low = 2
high = 6
s = Solution()
print(s.countPairs(nums,low,high))