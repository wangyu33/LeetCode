#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1815.py
# Author: WangYu
# Date  : 2021/4/6

import collections
from typing import List

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        n = len(groups)

        # 记录每组顾客的人数，对batchSize取模
        meno = [0] * batchSize
        for i, v in enumerate(groups):
            meno[v % batchSize] += 1

        # 模为0的顾客组，该组开心
        pre = meno[0]
        meno[0] = 0

        # 预处理一下，若两个组的人数和 被batchSize整除，则开心一次
        for i in range(batchSize):
            a, b = i, batchSize - i
            while meno[a] and meno[b]:
                if a == b and meno[a] < 2:
                    break
                meno[a] -= 1
                meno[b] -= 1
                pre += 1

        # print(n, meno)
        cache = {}

        def dfs(N, num):
            if (tuple(meno), num) in cache:
                return cache[(tuple(meno), num)]

            res = 0
            if N == 0:
                return 0
            if num != 0:
                next = batchSize - num
                if meno[next] > 0:
                    meno[next] -= 1
                    tmp = dfs(N - 1, 0)
                    meno[next] += 1
                    res = max(res, tmp)
                    cache[(tuple(meno), num)] = res
                    return res

            flag = 1 if num == 0 else 0
            for v in range(batchSize):
                if meno[v] > 0:
                    meno[v] -= 1
                    tmp = flag + dfs(N - 1, (num + v) % batchSize)
                    meno[v] += 1
                    res = max(res, tmp)
            cache[(tuple(meno), num)] = res
            return res

        res = dfs(sum(meno), 0)
        # print(res)

        # pre为递归前已经确定的最优开心数
        return pre + res

batchSize = 4
groups = [1,3,2,5,2,2,1,6]
s = Solution()
print(s.maxHappyGroups(batchSize, groups))