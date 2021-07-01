#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode25.py
# Author: WangYu
# Date  : 2021/3/15

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def creatListNode(nums):
    root = ListNode(nums[0])
    head = root
    for i in nums[1:]:
        tmp = ListNode(i)
        head.next = tmp
        head = head.next
    return root

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        top = ListNode(next=head)
        left = right = top

        while True:
            for _ in range(k):
                right = right.next
                if not right:
                    return top.next
            next_left = left.next
            for _ in range(k-1):
                left.next, right.next, right.next.next = left.next.next, left.next, right.next
            left = right = next_left

        return top

head = [1,2,3,4,5]
k = 2
s = Solution()
print(s.reverseKGroup(creatListNode(head),k))