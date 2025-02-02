#!/usr/bin/env python3
"""Reduce 4."""
import sys
import itertools


def reduce_one_group(doc_id, group):
    """Reduce TF-IDF scores for one group of terms."""
    term_scores = []
    w = 0

    for line in group:
        _, idf, term, tf = line.strip().split("\t")
        tf = float(tf)
        idf = float(idf)
        w += (tf * idf) ** 2
        term_scores.append((term, tf, idf))

    d_2 = w

    for term, tf, idf in term_scores:
        print(f"{term}\t{idf}\t{doc_id}\t{int(tf)}\t{d_2}")


def keyfunc(line):
    """Return the key for grouping lines."""
    return line.strip().split("\t")[0]


def main():
    """Main function to process input."""
    for doc_id, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(doc_id, group)


if __name__ == "__main__":
    main()
