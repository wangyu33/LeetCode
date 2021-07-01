#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode5703.py
# Author: WangYu
# Date  : 2021/3/14

from typing import List
from queue import PriorityQueue
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pas = PriorityQueue()
        ret = []
        for i in range(len(classes)):
            if classes[i][0] == classes[i][1]:
                ret.append(1.0)
            else:
                df = (classes[i][0]+1)/(classes[i][1]+1) - classes[i][0]/classes[i][1]
                pas.put([-df, *classes[i]])
        while extraStudents > 0:
            stu1 = pas.get()
            stu1[1] += 1
            stu1[2] += 1
            stu1[0] = (stu1[1] + 1) / (stu1[2] + 1) - stu1[1] / stu1[2]
            stu1[0] *= -1
            extraStudents -= 1
            pas.put(stu1)
        while not pas.empty():
            stu = pas.get()
            ret.append(stu[1]/stu[2])
        return sum(ret)/len(ret)

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
s = Solution()
print(s.maxAverageRatio(classes,extraStudents))