#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1769.py
# Author: WangYu
# Date  : 2021/2/23

from functools import  lru_cache
from typing import  List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lru_cache()
        def gao(boxes, num, op):
            if num == 0 and op == 'l':
                return int(boxes[num])
            elif op == 'l':
                return gao(boxes,num-1,'l')*2 + int(boxes[num])
            elif num == len(boxes)-1 and op == 'r':
                return int(boxes[num])
            elif op == 'r':
                return gao(boxes,num+1,'r')*2 + int(boxes[num])
        ret = []
        sum(i * (b == '1') for i, b in enumerate(boxes))
        ret.append(sum(i * (b == '1') for i, b in enumerate(boxes)))
        for i in range(1, len(boxes)):
            temp = ret[-1] - gao(boxes,i,'r') + gao(boxes,i,'l')
            ret.append(temp)
        return ret

s = Solution()
boxes = "001011"
print(s.minOperations(boxes))