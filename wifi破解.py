#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : wifi破解.py
# Author: WangYu
# Date  : 2021/2/16

import itertools
key = '0123456789.qwertyuiopasdfghjklzxcvbnm'#密码包含这些字符
passwords = itertools.product(key,repeat = 6)
f = open('password.txt','a')
for i in passwords:
    f.write("".join(i))
    f.write('\n')
    print(i)
f.close()

