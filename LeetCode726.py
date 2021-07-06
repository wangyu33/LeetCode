#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode726.py
# Author: WangYu
# Date  : 2021/7/5

import re
from collections import defaultdict
class Solution:
    pt=re.compile("([A-Z][a-z]*)|([()])|(\d+)")
    def countOfAtoms(self, formula: str) -> str:
        formula=tuple(filter(bool,re.split(self.pt,formula)))
        total=defaultdict(int)
        stack=[1,]
        num=1
        for a in formula[::-1]:
            if a.isdigit():
                num=int(a)
            else:
                mul=stack[-1]
                if a.isalpha():
                    total[a] += mul*num
                elif ')'==a:
                    stack.append(mul*num)
                elif '('==a:
                    stack.pop()
                num=1
        return ''.join(key+(str(val) if val>1 else '')
                       for key,val in sorted(total.items()))

formula = "K4(ON(SO3)2)2"
s = Solution()
print(s.countOfAtoms(formula))