#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode143.py
# Author: WangYu
# Date  : 2020-10-20

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from functools import lru_cache
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:return
        # 找到中点
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转后半
        pre,cur = None,slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre,cur = cur,nxt
        # 交替合并
        p,q = head,pre
        while q:
            nxt = p.next
            p.next = q
            p,q = q,nxt
