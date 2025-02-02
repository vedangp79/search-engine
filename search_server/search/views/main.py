from flask import render_template, request
import requests
from concurrent.futures import ThreadPoolExecutor
import heapq
from search import app
from search import model

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "")
    weight = float(request.args.get("w", 0.5))
    hits = []
    if query:
        hits = get_docs(query, weight)
    return render_template("index.html", query=query, weight=weight, hits=hits)

def get_docs(query, weight):
    # Make concurrent requests to Index servers
    with ThreadPoolExecutor() as executor:
        # Use a ThreadPoolExecutor to dispatch requests to each Index server URL
        futures = [executor.submit(fetch_results, url, query, weight)
                   for url in app.config["SEARCH_INDEX_SEGMENT_API_URLS"]]

    # Final list that will accumulate the results from the futures using the heap merge
    results_lists = [future.result() for future in futures]

    # Using `heapq.merge` to merge the sorted results_lists into a single sorted results iterator
    sorted_iter = heapq.merge(*results_lists, key=lambda x: x['score'], reverse=True)

    # Convert the iterator to a list and get the top 10 hits
    # Note: heapq.merge returns a generator, so we need to use 'list' and slicing to get the top hits
    top_hits = list(sorted_iter)[:10]

    # Retrieve document details from the database
    doc_ids = [hit["docid"] for hit in top_hits]
    documents = model.get_documents(doc_ids)

    # Prepare the final search results with details populated from the documents
    return_results = []
    for hit, document in zip(top_hits, documents):
        return_val = {
            "title": document["title"],
            "url": document["url"],
            "summary": document.get("summary", "No summary available"),
        }
        return_results.append(return_val)

    return return_results


def fetch_results(url, query, weight):
    response = requests.get(url, params={"q": query, "w": weight})
    if response.status_code == 200:
        return response.json()["hits"]
    return []