#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode39.py
# Author: WangYu
# Date  : 2020-09-09

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        def dfs(tar, start, temp: List[int]):
            if start >= len(candidates):
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num + tar > target:
                    break
                if (target - tar) // num > 0:
                    for j in range(1, (target - tar) // num + 1):
                        if tar + num * j == target:
                            gao = temp[:]
                            gao.extend([num] * j)
                            ans.append(gao)
                            continue
                        else:
                            gao = temp[:]
                            gao.extend([num] * j)
                            dfs(tar + num * j, i + 1, gao)
        dfs(0, 0, [])
        return ans

candidates = [2,3,5]
target = 8
S = Solution()
print(S.combinationSum(candidates, target))