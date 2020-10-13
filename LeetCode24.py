#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode24.py
# Author: WangYu
# Date  : 2020-10-13
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second