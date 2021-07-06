#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1418.py
# Author: WangYu
# Date  : 2021/7/6

from typing import List
from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = defaultdict(lambda: defaultdict(int))
        foodname = set()
        table = set()
        for cus,tab, fod in orders:
            d[tab][fod]+=1
            foodname.add(fod)
            table.add(tab)
        foodname = list(foodname)
        foodname = sorted(foodname)
        table = sorted(list(table), key = lambda x:int(x))
        ans = ['Table']
        ans.extend(foodname)
        for i in table:
            tmp = [str(i)]
            for fod in foodname:
                tmp.append(str(d[i][fod]))
            ans.append(tmp)
        return ans

s = Solution()
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(s.displayTable(orders))