
from sentence_transformers import SentenceTransformer


# Load the embedding model
embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embeddings(texts):
    embeddings = embedding_model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings
