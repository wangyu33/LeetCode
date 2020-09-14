#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1585.py
# Author: WangYu
# Date  : 2020-09-14
from collections import *
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False

        cnt = [0] * 10
        dn2cnt = defaultdict(deque)
        for i, c in enumerate(t):
            n = ord(c) - ord('0')
            dn2cnt[n].append(cnt[:])
            cnt[n] += 1

        cnt = [0] * 10
        for i, c in enumerate(s):
            n = ord(c) - ord('0')
            cnt1 = dn2cnt[n].popleft()
            for j in range(n + 1, 10):
                if cnt[j] < cnt1[j]:
                    return False
            cnt[n] += 1
        return True