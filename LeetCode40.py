#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode40.py
# Author: WangYu
# Date  : 2020-09-10

from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        target = n
        candidates = [1,2,3,4,5,6,7,8,9]
        ans = []

        def dfs(tar, start, temp: List[int]):
            if len(temp) > k:
                return
            if len(temp) == k and sum(temp) == target:
                ans.append(temp)
                return
            elif len(temp) == k and sum(temp) != target:
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num + tar > target:
                    break
                if (target - tar) // num > 0:
                    gao = temp[:]
                    gao.extend([num])
                    dfs(tar + num, i + 1, gao)

        dfs(0, 0, [])
        dic = list(set([tuple(t) for t in ans]))
        ans = list(list(t) for t in dic)
        return ans


k = 3
n = 9
S = Solution()
print(S.combinationSum3(k, n))