#!/usr/bin/env python3
"""Reduce 0."""

import sys

# Initialize COUNT variable
COUNT = 0

# Iterate over input from stdin
for line in sys.stdin:
    # Split the line into key and value
    key, value = line.strip().split("\t")

    # Check if the key is "doc"
    if key == "document":
        # Increment the COUNT
        COUNT += int(value)

# Print the total COUNT of documents
print(COUNT)
