#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1707.py
# Author: WangYu
# Date  : 2021/1/21

from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        i = 0
        res = [-1]*len(queries)
        tmp = []
        depth = len(bin(max(nums)))-2
        nums.sort()
        for p,(x,m) in sorted(enumerate(queries), key = lambda x:x[1][1]):
            while(i<len(nums) and nums[i]<=m):
                nums_i = nums[i]
                cur = tmp
                for d in range(31,-1,-1):
                    if not cur:
                        cur.append([])
                        cur.append([])
                    temp = (nums_i>>d)&1
                    cur = cur[(nums_i>>d)&1]
                cur.append(nums_i)
                i+=1
            cur = tmp
            if not tmp:
                res[p]=-1
                continue
            for d in range(31,-1,-1):
                choice = (x>>d)&1^1
                if(not cur[choice]):
                    choice^=1
                cur = cur[choice]
            res[p]=x^cur[0]
        return res

s = Solution()
nums = [0,1,2,3,4]
queries = [[3,1],[1,3],[5,6]]
print(s.maximizeXor(nums,queries))
