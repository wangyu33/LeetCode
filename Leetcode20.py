#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Leetcode20.py
# Author: WangYu
# Date  : 2020-08-14

class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        dict = [s[0]]
        for str in s[1:]:
            if str == ']':
                if len(dict) == 0 or dict[-1] != '[':
                    return False
                dict.pop()
                continue
            if str == ')':
                if len(dict) == 0 or dict[-1] != '(':
                    return False
                dict.pop()
                continue
            if str == '}':
                if len(dict) == 0 or dict[-1] != '{':
                    return False
                dict.pop()
                continue
            if str == '[' or '(' or '}':
                dict.append(str)
        if len(dict) > 0:
            return False
        return True

str = "()]"
solution = Solution()
print(solution.isValid(str))

