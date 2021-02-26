#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1702.py
# Author: WangYu
# Date  : 2021/1/23

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        binary = list(binary)
        if '0' in binary:
            index = binary.index('0') + 1
        else:
            return binary
        for i in range(len(binary) - 1):
            if index >= len(binary):
                return ''.join(binary)
            if binary[i] == '1':
                continue
            while binary[index] == '1':
                index += 1
                if index >= len(binary):
                    return ''.join(binary)
            if index == i + 1:
                binary[i] = '1'
                binary[index] = '0'
                index += 1
            else:
                binary[i] = '1'
                binary[i + 1] = '0'
                binary[index] = '1'
                index += 1
        return ''.join(binary)

s = Solution()
binary = "01"
print(s.maximumBinaryString(binary))
