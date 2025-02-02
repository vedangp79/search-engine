#!/usr/bin/env python3
"""Map 3."""
import sys

for line in sys.stdin:
    doc_and_word, _, count = line.strip().partition("\t")
    doc_id, word = doc_and_word.split()
    print(f"{word}\t{doc_id}\t{count}")
