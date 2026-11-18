
from src.vector_store import (
    create_vector_store,
    search_similar_texts
)

documents = [
    "Python developer with machine learning experience.",
    "AI engineer building RAG and LLM applications.",
    "Java developer working on enterprise applications.",
    "Data scientist experienced in predictive analytics."
]

index = create_vector_store(documents)

query = "Experience developing AI applications using LLMs and RAG."

results = search_similar_texts(
    index,
    query,
    documents,
    top_k=3
)

print("\nFAISS Search Results:")

for result in results:
    print(result)
