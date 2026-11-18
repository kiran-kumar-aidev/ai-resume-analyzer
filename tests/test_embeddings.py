
from src.embeddings import generate_embeddings

texts = [
    "Python developer with experience in machine learning",
    "AI engineer experienced in building RAG applications",
    "Java developer working on enterprise applications"
]

embeddings = generate_embeddings(texts)

print("Number of text samples:", len(texts))
print("Embedding shape:", embeddings.shape)
print("First embedding:", embeddings[0][:10])
