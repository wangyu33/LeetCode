#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode1115.py
# Author: WangYu
# Date  : 2020-10-13
from threading import Lock
from threading import Thread

class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock1.acquire()

    def foo(self) -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lock2.acquire()
            print('Foo')
            self.lock1.release()

    def bar(self) -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.lock1.acquire()
            print('Bar')
            self.lock2.release()

s = FooBar(5)
t1 = Thread(target= s.foo)
t2 = Thread(target= s.bar)
t1.start()
t2.start()
t1.join()
t2.join()


