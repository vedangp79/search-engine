#!/usr/bin/env python3
"""Map 5."""
import sys

for line in sys.stdin:
    word, idf, doc_id, tf, d_2 = line.strip().split("\t")
    print(f"{word}\t{idf}\t{doc_id}\t{tf}\t{d_2}")
