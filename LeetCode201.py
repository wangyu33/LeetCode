#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode201.py
# Author: WangYu
# Date  : 2020-08-23

'''
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        m_list = []
        while m:
            m_list.append(m % 2)
            m = m //2
        n_list = []
        while n:
            n_list.append(n % 2)
            n = n //2
        if len(n_list) > len(m_list):
            return 0
        m_list = list(reversed(m_list))
        n_list = list(reversed(n_list))
        cnt = len(m_list) - 1
        ans = 0
        for i in range(len(m_list)):
            if m_list[i] == n_list[i]:
                if m_list[i] == 1:
                    ans = ans + 2**cnt
                cnt = cnt - 1
            else:
                break
        # print(ans)
        return ans

s = Solution()
s.rangeBitwiseAnd(2,2)