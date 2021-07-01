#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Vivo1.py
# Author: WangYu
# Date  : 2021/4/1

class Solution:
    def compileSeq(self, input):
        # write code here
        ret = []
        from collections import defaultdict
        son = defaultdict(list)
        input = list(map(int, input.split(',')))
        for i in range(len(input)):
            if input[i] != -1:
                son[input[i]].append(i)
            else:
                ret.append(i)
        ret = sorted(ret)
        tmp = ret
        while len(ret) < len(input):
            tmp1 = []
            for i in tmp:
                if len(son[i]) > 0:
                    son[i] = sorted(son[i])
                    index = ret.index(i) + 1
                    for j in son[i]:
                        while index < len(ret) and j > ret[index]:
                            index += 1
                        ret.insert(index, j)

            tmp1 = sorted(tmp1)
            tmp = tmp1
        ret = [str(i) for i in ret]
        return ','.join(ret)

ss = "8,2,7,4,6,-1,5,5,6"
s = Solution()
print(s.compileSeq(ss))