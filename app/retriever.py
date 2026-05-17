import json
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L3-v2')


def build_vectorstore():

    with open("../data/catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)

    documents = []

    for item in catalog:

        text = f"""
Name: {item['name']}
Description: {item['description']}
URL: {item['url']}
"""

        documents.append(text)

    embeddings = model.encode(documents)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, "../vectorstore/shl_index.faiss")

    with open("../vectorstore/documents.pkl", "wb") as f:
        pickle.dump(catalog, f)

    print("Vectorstore created successfully")


def search_assessments(query, top_k=5):

    index = faiss.read_index("../vectorstore/shl_index.faiss")

    with open("../vectorstore/documents.pkl", "rb") as f:
        documents = pickle.load(f)

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), top_k)

    results = []

    for idx in indices[0]:

        results.append(documents[idx])

    return results


if __name__ == "__main__":

    build_vectorstore()