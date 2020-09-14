#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1583.py
# Author: WangYu
# Date  : 2020-09-14

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        D = {}
        for i, r in enumerate(preferences):
            D[i] = r
        ans = 0

        def judge(a, num):
            for i in D[a][0:num]:
                for j in pairs:
                    if i not in j:
                        continue
                    if j[0] == i:
                        if D[i].index(a) < D[i].index(j[1]):
                            return True
                    if j[1] == i:
                        if D[i].index(a) < D[i].index(j[0]):
                            return True
            return False

        for i in pairs:
            a, b = i
            if judge(a, D[a].index(b)):
                ans += 1
            if judge(b, D[b].index(a)):
                ans += 1
        return ans

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
s = Solution()
print(s.unhappyFriends(n,preferences,pairs))


