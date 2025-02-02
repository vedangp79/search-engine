#!/usr/bin/env python3
"""Reduce 5."""
import sys
import itertools


def reduce_one_group(group):
    """Reduce TF-IDF scores for one group of terms."""
    group = list(group)
    head = group[0].strip().split("\t")
    if len(head) != 5:
        raise ValueError(f"Not five values in a column, got {len(head)}: {group[0]}")

    term, idfk = head[:2]
    output = f"{term} {idfk}"

    for line in group:
        _, _, doc_id, tf, d_2 = line.strip().split("\t")
        output += f" {doc_id} {tf} {d_2}"

    print(output)


def keyfunc(line):
    """keyfunc."""
    return line.strip().split("\t")[0]


def main():
    """Reduce TF-IDF scores for one group of terms."""
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(group)


if __name__ == "__main__":
    main()
