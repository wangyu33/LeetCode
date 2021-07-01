#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : meituan2021-8-1.py
# Author: WangYu
# Date  : 2021/3/15

# 小美的书架上有很多书。小美是个爱读书的新时代好青年。
#
# 小团虽然也喜欢看书，但小团大多数时候都更喜欢来小美家蹭书读。
#
# 这就导致小美的书架上很多书都会被小团借走。
#
# 小美很烦这一点，就想出了一个招数，小美的书架是一行一行的，他会对一些行加锁，这样小团就借不走了。
#
# 现在小团想要借书，请你帮忙看看小团能不能借到书，如果可以借到的话在哪一行书架上有这本书。
#
# 为了简单起见，每本书将用一个正整数进行编号，小美的书架一共有N行。

from collections import defaultdict
if __name__ == '__main__':
    n,m,q = list(map(int, input().split()))
    bookcase = defaultdict(list)
    book = defaultdict(int)
    lock = []
    for i in range(q):
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:
            if tmp[2] not in lock and book[tmp[1]]!=-1 and book[tmp[1]] not in lock:
                bookcase[tmp[2]].append(tmp[1])
                if book[tmp[1]] > 0:
                    bookcase[book[tmp[1]]].remove(tmp[2])
                book[tmp[1]] = tmp[2]
        elif tmp[0] == 2:
            if tmp[1] not in lock:
                lock.append(tmp[1])
        elif tmp[0] == 3:
            if tmp[1] in lock:
                lock.remove(tmp[1])
        elif tmp[0] == 4:
            if book[tmp[1]] not in lock and book[tmp[1]] > 0:
                print(book[tmp[1]])
                book[tmp[1]] = -1
            else:
                print(-1)
        elif tmp[0] == 5:
            if book[tmp[1]] == -1:
                book[tmp[1]] = 0