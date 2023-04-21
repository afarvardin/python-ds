from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def generate_embeddings(text):
    embeddings = model.encode(text)
    return [float(x) for x in embeddings.tolist()]


generate_embeddings(
    """
Web APIs are a huge opportunity to access and integrate data from any sources with your graph. Most of them provide the data in JSON format.

The Load JSON procedures retrieve data from URLs or maps and turn it into map value(s) for Cypher to consume. Cypher has support for deconstructing nested documents with dot syntax, slices, UNWIND etc. so it is easy to turn nested data into graphs.

Sources with multiple JSON objects (JSONL,JSON Lines) in a stream, like the streaming Twitter format or the Yelp Kaggle dataset, are also supported,
"""
)