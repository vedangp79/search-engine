#!/usr/bin/env python3
"""
Reduce 3.
"""

import sys
import math


def emit_output(word, document_ids, inverse_df):
    """
    Emit the output in the desired format.
    """
    for doc_id, tf in document_ids:
        print(f"{word}\t{doc_id}\t{tf}\t{inverse_df}")


def calculate_idf(total_document_count, document_ids_count):
    """
    Calculate inverse document frequency.
    """
    return math.log10(total_document_count / document_ids_count)


with open("total_document_count.txt", "r", encoding="utf-8") as file:
    total_docs = int(file.read().strip())

CURRENT_WORD = None
word_doc_ids = []

for line in sys.stdin:
    term, docu_id, tff = line.strip().split("\t")
    if term != CURRENT_WORD:
        if CURRENT_WORD:
            idf_value = calculate_idf(total_docs, len(word_doc_ids))
            emit_output(CURRENT_WORD, word_doc_ids, idf_value)
        CURRENT_WORD = term
        word_doc_ids = []
    word_doc_ids.append((docu_id, tff))

if CURRENT_WORD:
    idf_value = calculate_idf(total_docs, len(word_doc_ids))
    emit_output(CURRENT_WORD, word_doc_ids, idf_value)
