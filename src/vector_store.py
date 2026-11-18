
import faiss
import numpy as np

from src.embeddings import generate_embeddings


def create_vector_store(texts):

    embeddings = generate_embeddings(texts)

    embeddings = np.asarray(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index


def search_similar_texts(index, query, texts, top_k=3):

    query_embedding = generate_embeddings([query])

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    scores, indices = index.search(
        query_embedding,
        min(top_k, len(texts))
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx != -1:
            results.append({
                "text": texts[idx],
                "similarity_score": round(float(score), 4)
            })

    return results
