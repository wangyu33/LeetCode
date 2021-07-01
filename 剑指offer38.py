#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 剑指offer38.py
# Author: WangYu
# Date  : 2021/6/22

from typing import List
from collections import defaultdict


class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        ans = []
        d = defaultdict(int)

        def dfs(index, t, D):
            if index == len(s):
                ans.append(t)

            for i in range(len(s)):
                if D[i] == 0:
                    D[i] = 1
                    dfs(index + 1, t + s[i], D)
                    D[i] = 0

        dfs(0, '', d)
        return list(set(ans))

s = "abc"
S = Solution()
print(S.permutation(s))