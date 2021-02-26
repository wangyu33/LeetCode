#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode946.py
# Author: WangYu
# Date  : 2020-10-23

from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0:
            return True
        ans = [pushed[0]]
        push = 0
        pop = 0
        while push < len(pushed) and pop < len(popped):
            if len(ans) == 0:
                push += 1
                if push > len(pushed) - 1:
                    return False
                ans.append(pushed[push])
            elif popped[pop] != ans[-1]:
                push += 1
                if push > len(pushed) - 1:
                    return False
                ans.append(pushed[push])

            else:
                ans.pop(-1)
                pop += 1
        if len(ans) == 0:
            return True
        return False

s = Solution()
a = [1,0]
b = [1,0]
s.validateStackSequences(a,b)
