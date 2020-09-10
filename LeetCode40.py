#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode40.py
# Author: WangYu
# Date  : 2020-09-10

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                    for j in range(1, min((target - tar) // num + 1, 2)):
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
        dic = list(set([tuple(t) for t in ans]))
        ans = list(list(t) for t in dic)
        return ans

candidates = [2,5,2,1,2]
target = 5
S = Solution()
print(S.combinationSum2(candidates, target))