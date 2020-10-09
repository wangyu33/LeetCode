#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1609.py
# Author: WangYu
# Date  : 2020-10-07

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        tree = [root]
        flag = 0
        while tree:
            nums = []
            temp = []
            for i in tree:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
                nums.append(i.val)
            tree = temp
            print(nums)
            print(flag)
            if flag == 0:
                flag = 1
                for i in range(1, len(nums)):
                    if nums[i-1] > nums[i]:
                        return False
            if flag == 1:
                flag = 0
                for i in range(1, len(nums)):
                    if nums[i-1] < nums[i]:
                        return False
        return True
S = Solution()
root = TreeNode(1)
root.left = TreeNode(10)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(12)
root.left.left.right = TreeNode(8)
root.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(9)
root.right.right.right = TreeNode(2)
print(S.isEvenOddTree(root))