#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1593.py
# Author: WangYu
# Date  : 2020-09-21

from collections import defaultdict
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.ans = 1
        self.dfs(s, [])
        return self.ans

    def dfs(self, s, path):
        if len(set(path)) != len(path):
            return
        if not s:  ## 满足条件的划分更新self.ans
            self.ans = max(self.ans, len(path))
            return

        for i in range(len(s)):
            self.dfs(s[i + 1:], path + [s[:i + 1]])



s = Solution()
s1 = "addbsd"
print(s.maxUniqueSplit(s1))