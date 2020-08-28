#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode17.py
# Author: WangYu
# Date  : 2020-08-26

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dict = {}
        dict['2'] = 'abc'
        dict['3'] = 'def'
        dict['4'] = 'ghi'
        dict['5'] = 'jkl'
        dict['6'] = 'mno'
        dict['7'] = 'pqrs'
        dict['8'] = 'tuv'
        dict['9'] = 'wxyz'
        ans = [i for i in dict[digits[0]]]
        for s in digits[1:]:
            s_list = [i for i in dict[s]]
            temp = [i+j for i in ans for j in s_list]
            ans = temp

        return ans

s = Solution()
S = "234"
print(s.letterCombinations(S))

