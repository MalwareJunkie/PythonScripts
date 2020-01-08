#!/usr/bin/env python3

"""
    WARNING: Before you run this script you should know that it will attempt to connect to the provided URL
"""

import sys
import urllib.request

if len(sys.argv) != 2:
    print("Usage: {0} <shortenedURL>".format(sys.argv[0]))
else:
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.geturl())
