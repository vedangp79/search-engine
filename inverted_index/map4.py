#!/usr/bin/env python3
"""Map 4."""
import sys

for line in sys.stdin:
    word, doc_id, tf, idf = line.strip().split("\t")
    print(f"{doc_id}\t{idf}\t{word}\t{tf}")
