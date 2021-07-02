#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File    : LeetCode224.py
# Author  : WangYu
# Date    : 2021/3/10

from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        sDeque = deque(s)
        def helper(sDeque) -> int:
            num = 0
            sign = "+"
            stack = []
            while len(sDeque) > 0:
                # 注意 这里需要从头部开始pop
                char = sDeque.popleft()
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(sDeque)
                if (not char.isdigit() and char != " ") or len(sDeque) == 0:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    # 重置num和sign
                    num = 0
                    sign = char
                if char == ")":
                    break
            return sum(stack)
        return helper(sDeque)


s = "(1+(4+5+2)-3)+(6+8)"
S = Solution()
print(S.calculate(s))
