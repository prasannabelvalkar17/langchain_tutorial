from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

## Huggingface model download local path C:\Users\username\.cache\huggingface\hub

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is capital of India"

vector = embedding.embed_query(text)

print(str(vector))


print("#############  Embedding documents   #############")

from sentence_transformers import SentenceTransformer

embedding_document = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = ["Delhi is capital of India", "Mumbai is capital of Maharashtra"]

embedded_documents = embedding_document.encode(documents)

print(embedded_documents)

print("#############  Similarity Search   #############")

from sklearn.metrics.pairwise import cosine_similarity

question = "tell me about Mumbai"
embedded_question = embedding_document.encode([question])
similarity = cosine_similarity(embedded_question, embedded_documents)[0]
print(similarity)

import numpy as np

sorted_similarity = sorted(list(enumerate(similarity)), key=lambda x: x[1], reverse=True)
print(sorted_similarity)

index, myscore = sorted_similarity[0]

print("Question: ", question)

print(f"Most similar document is: {documents[index]} with score: {myscore}")
