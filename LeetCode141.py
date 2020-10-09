#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode141.py
# Author: WangYu
# Date  : 2020-10-09

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        D = defaultdict(int)
        while head:
            # print(head.val)
            if D[head] == 0:
                D[head] = 1
                head = head.next
            else:
                return True
        return False