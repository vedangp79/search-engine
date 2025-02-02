import sqlite3
import csv
import pathlib
from search import app

stopwords = []
pageranks = {}
inverted_index = {}

def load_stopwords():
    global stopwords
    stopwords_path = pathlib.Path(app.config["INDEX_DIR"]).parent / "stopwords.txt"
    with open(stopwords_path, "r") as file:
        stopwords = file.read().splitlines()

def load_pageranks():
    global pageranks
    pagerank_path = pathlib.Path(app.config["INDEX_DIR"]).parent / "pagerank.out"
    with open(pagerank_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            doc_id, score = row
            pageranks[int(doc_id)] = float(score)

def load_inverted_index():
    global inverted_index
    index_dir = pathlib.Path(app.config["INDEX_DIR"])
    for i in range(3):
        file_path = index_dir / f"inverted_index_{i}.txt"
        with open(file_path, "r") as file:
            for line in file:
                term, *postings = line.strip().split()
                idf = float(postings[0])
                inverted_index[term] = {"idf": idf}

def load_data():
    load_stopwords()
    load_pageranks()
    load_inverted_index()

def get_db():
    db = sqlite3.connect("var/search.sqlite3")
    db.row_factory = sqlite3.Row
    return db

def get_documents(doc_ids):
    db = get_db()
    placeholders = ",".join(["?" for _ in doc_ids])
    query = f"SELECT * FROM documents WHERE docid IN ({placeholders})"
    documents = db.execute(query, doc_ids).fetchall()
    return [dict(row) for row in documents]