#!/usr/bin/env -S python3 -u
"""Partition."""
import sys

for line in sys.stdin:
    key = line.strip().split("\t")[2]
    print(int(key) % 3)
