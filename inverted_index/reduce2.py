#!/usr/bin/env python3
"""Reduce 2."""
import sys

CURRENT_KEY = None
COUNT = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key != CURRENT_KEY:
        if CURRENT_KEY:
            print(f"{CURRENT_KEY}\t{COUNT}")
        CURRENT_KEY = key
        COUNT = 0
    COUNT += int(value)

if CURRENT_KEY:
    print(f"{CURRENT_KEY}\t{COUNT}")
