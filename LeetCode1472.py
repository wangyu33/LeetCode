#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1472.py
# Author: WangYu
# Date  : 2021/4/2

class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = 0
        self.forw =[]
        self.ba = []
        self.now = homepage

    def visit(self, url: str) -> None:
        self.ba.append(self.now)
        self.now = url
        self.forw =[]

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.ba) == 0:
                break
            else:
                self.forw.append(self.now)
                self.now = self.ba[-1]
                self.ba.pop(-1)
        return self.now

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if len(self.forw) == 0:
                break
            else:
                self.ba.append(self.now)
                self.now = self.forw[-1]
                self.forw.pop(-1)
        return self.now


obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
param_1 = obj.back(1)
param_2 = obj.back(1)
param_3= obj.forward(1)
obj.visit("linkedin.com")
param_4 = obj.forward(2)
param_5 = obj.back(2)
param_6 = obj.back(7)
print()