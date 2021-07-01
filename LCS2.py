#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LCS2.py
# Author: WangYu
# Date  : 2021/6/21
from typing import List
class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        from collections import Counter
        C = Counter(questions).most_common()
        # C = sorted(C, key = lambda x:x[1])
        cnt = 0
        num = 0
        for key,n in C:
            num += n
            if num >= len(questions)/2:
                return cnt+1
            cnt+=1

questions = [2,1,6,2]
s = Solution()
print(s.halfQuestions(questions))
