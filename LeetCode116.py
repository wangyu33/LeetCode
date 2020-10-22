#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode116.py
# Author: WangYu
# Date  : 2020-10-15

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        tree = [root]
        while tree:
            temp = []
            for index, t in enumerate(tree):
                if index != len(tree) - 1:
                    tree[index].next = tree[index + 1]
                else:
                    tree[index] = None
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
            tree = temp
        return root