#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1611.py
# Author: WangYu
# Date  : 2020-10-07
from functools import lru_cache
import math
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @lru_cache(None)
        def calc(k):
            if k == 0:
                return 0
            if k == 1:
                return 1
            if k == 2:
                return 3
            if k == 3:
                return 2
            klog = int(math.log2(k))
            if k == 1<<klog:
                return (1<<(klog + 1)) -1
            if k - (1<<klog) >= (1<<(klog-1)):
                return calc(1<<(klog-1)) + 1 + calc(k - (1<<klog) - (1<<(klog-1)))
            elif k - (1<<klog) < (1<<(klog-1)):
                return 2 * calc(1<<(klog-1)) + 1 - calc(k - (1<<klog))
        return calc(n)
