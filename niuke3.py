#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : niuke3.py
# Author: WangYu
# Date  : 2021/1/22

'''
现在有n个人排队买票，已知是早上8点开始卖票，这n个人买票有两种方式：

第一种是每一个人都可以单独去买自己的票，第 i 个人花费 a[i] 秒。

第二种是每一个人都可以选择和自己后面的人一起买票，第 i 个人和第 i+1 个人一共花费 b[i] 秒。

最后一个人只能和前面的人一起买票或单独买票。

由于卖票的地方想早些关门，所以他想知道他最早几点可以关门，请输出一个时间格式形如：08:00:40 am/pm

时间的数字要保持 2 位，若是上午结束，是 am ，下午结束是 pm


输入描述:
第一行输入一个整数 T，接下来有 T 组测试数据。

对于每一组测试数据：输入一个数 n，代表有 n 个人买票。

接下来n个数，代表每一个人单独买票的时间 a[i]。

接下来 n-1 个数，代表每一个人和他前面那个人一起买票需要的时间 b[i]
1<= T <=100
1<= n <=2000
1<= a[i] <=50
1<= b[i] <=50
'''


def main():
    global a, ans, asum, asum0
    T = int(input())
    for t in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        time = 0
        b = list(map(int, input().split()))
        if n == 1:
            time += sum(a)
            s = time%60
            minu = time//60 %60
            hour = time // 3600 + 8
            s = '0' * (2 - len(str(s))) + str(s)
            minu = '0' * (2 - len(str(minu))) + str(minu)
            if hour > 12:
                hour -= 12
                hour = '0' * (2 - len(str(hour))) + str(hour)
                print('{}:{}:{} pm'.format(hour,minu,s))
            else:
                hour = '0' * (2 - len(str(hour))) + str(hour)
                print('{}:{}:{} am'.format(hour, minu, s))
        else:
            dp = [0] * (n+1)
            dp[1] = a[0]
            for i in range(2,n+1):
                dp[i] = min(dp[i-2]+b[i-2],dp[i-1]+a[i-1])
            time = dp[-1]
            s = time % 60
            minu = time // 60 % 60
            hour = time // 3600 + 8
            s = '0'*(2-len(str(s))) + str(s)
            minu = '0' * (2 - len(str(minu))) + str(minu)
            if hour > 12:
                hour -= 12
                hour = '0' * (2 - len(str(hour))) + str(hour)
                print('{}:{}:{} pm'.format(hour, minu, s))
            else:
                hour = '0' * (2 - len(str(hour))) + str(hour)
                print('{}:{}:{} am'.format(hour, minu, s))

if __name__ == '__main__':
    main()