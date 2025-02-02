#!/usr/bin/env python3
"""Map 1."""
import sys
import hashlib
import bs4

HASH_ALGORITHM = "sha512"

# Parse one HTML document at a time.  Note that this is still O(1) memory
# WRT the number of documents in the dataset.
HTML = ""
for line in sys.stdin:
    # Assume well-formed HTML docs:
    # - Starts with <!DOCTYPE html>
    # - End with </html>
    # - Contains a trailing newline
    if "<!DOCTYPE html>" in line:
        HTML = line
    else:
        HTML += line

    # If we're at the end of a document, parse
    if "</html>" not in line:
        continue

    # Configure Beautiful Soup parser
    soup = bs4.BeautifulSoup(HTML, "html.parser")

    # Parse content from document
    # get_text() will strip extra whitespace and
    # concatenate content, separated by spaces
    element = soup.find("html")
    content = element.get_text(separator=" ", strip=True)
    content = content.replace("\n", "")

    hash_obj = hashlib.new(HASH_ALGORITHM)
    hash_obj.update(content.encode("utf-8"))
    doc_id = int(hash_obj.hexdigest(), 16) % (10**7)

    print(f"{doc_id}\t{content}")
