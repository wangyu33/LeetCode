#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode763.py
# Author: WangYu
# Date  : 2020-10-22

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        num = Counter(S)
        start = 0
        D = defaultdict(int)
        ans = []
        for i in range(len(S)):
            D[S[i]] += 1
            flag = 1
            for k in D:
                if D[k] != num[k]:
                    flag = 0
                    break
            if flag:
                D = defaultdict(int)
                ans.append(len(S[start:i+1]))
                # print(start)
                start = i + 1
        return ans