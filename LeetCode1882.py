#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1882.py
# Author: WangYu
# Date  : 2021/5/31

import heapq
from  typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # 工作中的服务器，存储二元组 (t, idx)
        busy = list()

        # 空闲的服务器，存储二元组 (w, idx)
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)

        ts = 0

        # 将优先队列 busy 中满足 t<=ts 依次取出并放入优先队列 idle
        def release():
            while busy and busy[0][0] <= ts:
                _, idx = heapq.heappop(busy)
                heapq.heappush(idle, (servers[idx], idx))

        ans = list()
        for i, task in enumerate(tasks):
            ts = max(ts, i)
            release()
            if not idle:
                ts = busy[0][0]
                release()

            _, idx = heapq.heappop(idle)
            ans.append(idx)
            heapq.heappush(busy, (ts + task, idx))

        return ans


servers = [5,1,4,3,2]
tasks = [2,1,2,4,5,2,1]
s = Solution()
print(s.assignTasks(servers,tasks))