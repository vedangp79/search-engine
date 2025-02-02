#!/usr/bin/env python3
"""Map 2."""
import re
import sys


def clean_text(text):
    """Clean text."""
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    text = text.casefold()
    terms = text.split()
    with open("stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().splitlines()
    terms = [term for term in terms if term not in stopwords]
    return terms


for line in sys.stdin:
    doc_id, _, content = line.partition("\t")
    clean_terms = clean_text(content)
    for term in clean_terms:
        print(f"{doc_id} {term}\t1")
