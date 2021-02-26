#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode234.py
# Author: WangYu
# Date  : 2020-10-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans == ans[::-1]