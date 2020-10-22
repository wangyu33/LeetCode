#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode977.py
# Author: WangYu
# Date  : 2020-10-16

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        k = [abs(i) for i in A]
        return [i*i for i in sorted(k)]