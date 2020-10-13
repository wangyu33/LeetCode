#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1616.py
# Author: WangYu
# Date  : 2020-10-12

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a)<=1:
            return True
        if a == a[::-1] or b == b[::-1]:
            return True
        # a = list(a)
        # b = list(b)
        cnt1 = 0
        cnt2 = len(a) - 1
        while cnt1 <= cnt2:
            # print(a[cnt1],b[cnt2])
            if a[cnt1] != b[cnt2]:
                break
            cnt1 += 1
            cnt2 -= 1
        temp = a[:cnt1] + b[cnt1:]
        temp1 = a[:len(a)-cnt1] + b[len(a)-cnt1:]
        # print(temp1)
        if cnt1 >= cnt2 or temp == temp[::-1] or temp1 == temp1[::-1]:
            return True
        cnt1 = 0
        cnt2 = len(a) - 1
        while cnt1 <= cnt2:
            # print(b[cnt1],a[cnt2])
            if b[cnt1] != a[cnt2]:
                break
            cnt1 += 1
            cnt2 -= 1
        temp = b[:cnt1] + a[cnt1:]
        temp1 = b[:len(a)-cnt1] + a[len(a)-cnt1:]
        # print(temp)
        if cnt1 >= cnt2 or temp == temp[::-1] or temp1 == temp1[::-1]:
            return True
        return False