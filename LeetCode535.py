#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : LeetCode535.py
# Author: WangYu
# Date  : 2020-10-21

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl.encode('utf-8')

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl.decode('utf-8')