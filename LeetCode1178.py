#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1178.py
# Author: WangYu
# Date  : 2021/2/26

from typing import *
from collections import defaultdict
from functools import lru_cache
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         dp = defaultdict(list)
#         dw = defaultdict(list)
#
#         @lru_cache(None)
#         def gao(d, s):
#             for i in range(len(d)):
#                 if d[i] == s:
#                     return True
#             return False
#
#         for i in range(len(puzzles)):
#             tmp = set()
#             for j in range(len(puzzles[i])):
#                 tmp.add(puzzles[i][j])
#             dp[i] = tuple(tmp)
#
#         for i in range(len(words)):
#             tmp = set()
#             for j in range(len(words[i])):
#                 tmp.add(words[i][j])
#             dw[i] = tuple(tmp)
#
#         ret = []
#         for i in range(len(puzzles)):
#             cnt = 0
#             for j in range(len(words)):
#                 # print(dw[j], puzzles[i][0])
#                 if gao(dw[j], puzzles[i][0]):
#                     flag = 1
#                     for k in dw[j]:
#                         if not gao(dp[i], k):
#                             flag = 0
#                             break
#                     cnt += flag
#             ret.append(cnt)
#         gao.cache_clear()
#         return ret
import itertools
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        w = [frozenset(i) for i in words if len(set(i)) <= 7]
        d = {}
        res = []
        for i in w:
            d[i] = d.get(i, 0) + 1
        for p in puzzles:
            ct = 0
            pr = (p[0],)
            p = set(p[1:])
            tmp = 0
            for i in range(len(p)+1):
                for c in itertools.combinations(p, i):
                    tmp += 1
                    ct += d.get(frozenset(c+pr), 0)
            res.append(ct)
        return res


words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
s = Solution()
print(s.findNumOfValidWords(words,puzzles))

