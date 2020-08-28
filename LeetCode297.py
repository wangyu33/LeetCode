#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode297.py
# Author: WangYu
# Date  : 2020-08-26

'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
边界条件
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        #层序遍历
        from collections import deque
        tree_list = deque()
        tree_list.append(root)
        s = []
        while tree_list:
            if tree_list[0]:
                s.append(str(tree_list[0].val))
                tree_list.append(tree_list[0].left)
                tree_list.append(tree_list[0].right)
            else:
                s.append('null')
            tree_list.popleft()
        return ','.join(s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        if len(data) == 0 or data[0] == 'null':
            return []
        print(data)
        root = TreeNode(int(data[0]))
        from collections import deque
        tree_list = deque()
        tree_list.append(root)
        cnt = 1
        while tree_list:
            if data[cnt] != 'null':
                tree_list[0].left = TreeNode(int(data[cnt]))
                tree_list.append(tree_list[0].left)
            cnt = cnt + 1
            if data[cnt] != 'null':
                tree_list[0].right = TreeNode(int(data[cnt]))
                tree_list.append(tree_list[0].right)
            tree_list.popleft()
            cnt = cnt + 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

s = Codec()
list = [3,9,20,'null','null',15,7]
tree = TreeNode(5)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(2)
tree.right.right = TreeNode(4)
tree.right.left.left = TreeNode(3)
tree.right.left.right = TreeNode(1)
print(s.deserialize(s.serialize(tree)))


