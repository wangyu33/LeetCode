#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode49.py
# Author: WangYu
# Date  : 2020/12/14
from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        ans.append([])

        # print(ans)
        def dfs(s):
            flag = 0
            for i in strs.copy():
                if d[s] == d[i]:
                    ans[-1].append(i)
                    strs.remove(i)
                    s = i
                    flag = 1
            if len(strs) > 0:
                ans.append([])

        d = {}
        for i in strs:
            d[i] = Counter(i)

        while len(strs) > 0:
            # print(len(strs))
            temp = strs[0]
            ans[-1].append(temp)
            strs.remove(temp)
            dfs(temp)
        return ans

s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s.groupAnagrams(strs)