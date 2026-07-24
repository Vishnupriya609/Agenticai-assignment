from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from ollama import chat

# Read the document
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the document into chunks
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

documents = splitter.create_documents([text])

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in FAISS
db = FAISS.from_documents(documents, embeddings)

# User question
question = input("Ask a question: ")

# Retrieve relevant chunks
results = db.similarity_search(question, k=2)

context = "\n".join([doc.page_content for doc in results])

# Build prompt
prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

# Generate answer with Ollama
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nAnswer:\n")
print(response.message.content)