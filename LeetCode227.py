#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File    : LeetCode227.py
# Author  : WangYu
# Date    : 2021/3/11

class Solution:
    def calculate(self, s: str) -> int:
        s = s+'+'
        flag = "+"
        num = 0
        ret = []
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] in ['+','-','*','/']:
                if flag == '+':
                    ret.append(num)
                    num = 0
                elif flag == '-':
                    ret.append(-num)
                    num = 0
                elif flag == '*':
                    ret[-1] = ret[-1]*num
                    num = 0
                elif flag == '/':
                    ret[-1] = int(ret[-1]/num)
                    num = 0
                flag = s[i]
        return sum(ret)

ss = " 3+5 / 2 "
S = Solution()
print(S.calculate(ss))