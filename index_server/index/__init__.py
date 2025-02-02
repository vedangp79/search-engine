"""__init__.py."""
import os
from flask import Flask

app = Flask(__name__)

# Set the INDEX_PATH configuration
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")

import index.api  # noqa: E402  pylint: disable=wrong-import-position
