#!/usr/bin/env python3
"""Map 0."""
import sys

COUNT = 0
for line in sys.stdin:
    if "<!DOCTYPE html>" in line:
        COUNT += 1
print(f"document\t{COUNT}")
