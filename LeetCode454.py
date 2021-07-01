#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode454.py
# Author: WangYu
# Date  : 2021/3/30

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        nums = [A,B,C,D]
        global cnt
        cnt = 0
        def gao(idx,L):
            global cnt
            if idx == 4:
                if sum(L) == 0:
                    cnt += 1
                return
            tmp = L + [nums[idx][0]]
            gao(idx+1, tmp)
            tmp = L + [nums[idx][1]]
            gao(idx+1, tmp)
        gao(0,[])
        return cnt