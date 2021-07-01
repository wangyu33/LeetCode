#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1834.py
# Author: WangYu
# Date  : 2021/4/19

from typing import List
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tmp = []
        for i in range(len(tasks)):
            j = [tasks[i][1]]+ [i] +[tasks[i][0]]
            tmp.append(j)
        tasks = sorted(tmp, key = lambda x:(x[2],x[0]))
        # print(tasks)
        ans = []
        # time = heapq.
        time = 0
        ret = [tasks[0]]
        heapq.heapify(ret)
        tasks.pop(0)
        while ret or tasks:
            if ret:
                tmp = ret[0]
                heapq.heappop(ret)
                time = max(tmp[2],time) + tmp[0]
                ans.append(tmp[1])
            else:
                ret = [tasks[0]]
                tasks.pop(0)
                continue
            while tasks and tasks[0][2] <= time:
                heapq.heappush(ret, tasks[0])
                tasks.pop(0)
        return ans

s = Solution()
tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
print(s.getOrder(tasks))