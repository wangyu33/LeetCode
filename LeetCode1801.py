#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1801.py
# Author: WangYu
# Date  : 2021/3/22

from typing import List
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        from queue import PriorityQueue
        buy = PriorityQueue()
        sell = PriorityQueue()
        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and  not sell.empty():
                    s = sell.get()
                    if s[1] > amount and s[0] <= price:
                        sell.put([s[0],s[1]-amount])
                        amount = 0
                    elif s[1] <= amount and s[0] <= price:
                        amount -= s[1]
                    elif s[0] > price:
                        buy.put([-price, amount])
                        sell.put(s)
                        break
                if sell.empty() and amount > 0:
                    buy.put([-price, amount])
            if orderType == 1:
                while amount > 0 and  not buy.empty():
                    s = buy.get()
                    if s[1] > amount and price + s[0] <= 0:
                        buy.put([s[0],s[1]-amount])
                        amount = 0
                    elif s[1] <= amount and price + s[0] <= 0:
                        amount -= s[1]
                    elif price + s[0] > 0:
                        sell.put([price, amount])
                        buy.put(s)
                        break
                if buy.empty() and amount > 0:
                    sell.put([price, amount])
        cnt = 0
        while not sell.empty():
            s = sell.get()
            cnt = cnt + s[1]
        while not buy.empty():
            s = buy.get()
            cnt = (cnt+s[1])
        return int(cnt%(1e8+7))

orders = [[27,7,1],[6,27,0],[13,7,1],[4,7,1],[19,7,1],[4,22,1],[10,17,1],[1,11,1],[29,10,0],[6,7,1]]
s = Solution()
print(s.getNumberOfBacklogOrders(orders))