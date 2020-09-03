#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode841.py
# Author: WangYu
# Date  : 2020-08-31

'''
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keys-and-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import defaultdict
        room_num = len(rooms)
        d = defaultdict(int)
        d[0] = 1
        keys = rooms[0]
        while keys:
            key = keys[0]
            if d[key] != 1:
                keys.extend(rooms[key])
            d[key] = 1
            keys.pop(0)
        for i in range(room_num):
           if d[i] == 0:
                return False
        return True

room = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
s = Solution()
print(s.canVisitAllRooms(room))