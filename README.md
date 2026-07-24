# Applied Agenticai-assignment


# Overview

This project demonstrates the fundamentals of Applied Agentic AI using **Ollama** and the **Llama 3.2** model. The assignment includes:

1. LLM Workflow
2. Prompt Chaining
3. Agentic AI
4. Retrieval-Augmented Generation (RAG)

The implementation uses Python and runs locally through Ollama without requiring an external API key.

---

# Technologies Used

- Python 3.10+
- Ollama
- Llama 3.2
- FAISS
- Sentence Transformers
- LangChain (optional, if used)

---

# Structure

```
AgenticAI/
│
├── llm_workflow.py
├── prompt_chaining.py
├── agentic_ai.py
├── rag.py
├── sample.txt
├── requirements.txt
└── README.md
```

---

# 1. LLM Workflow

### Description

This program accepts user input and generates a response using the Llama 3.2 model running locally through Ollama.

### Features

- Accepts user input
- Sends prompt to the LLM
- Displays generated response

---

# 2. Prompt Chaining

### Description

This module demonstrates prompt chaining by performing multiple sequential LLM tasks.

Workflow:

1. Generate Summary
2. Extract Key Points
3. Generate Three Questions

Each step uses the previous step's output.

---

# 3. Agentic AI

### Description

A simple AI agent that:

- Accepts a task
- Creates a plan
- Executes the plan
- Produces the final output

---

# 4. RAG (Retrieval-Augmented Generation)

### Description

The RAG application:

- Reads a TXT document
- Splits the document into chunks
- Creates vector embeddings
- Retrieves relevant content
- Sends retrieved context to the LLM
- Generates an answer

---

# Requirements

Install the required packages:

```bash
pip install ollama
pip install faiss-cpu
pip install sentence-transformers
pip install pypdf
```

If your RAG implementation uses LangChain:

```bash
pip install langchain
pip install langchain-community
```

---

# Running the tasks

## Step 1

Start Ollama.

## Step 2

Download the model (only once):

```bash
ollama pull llama3.2
```

## Step 3

Run the programs:

LLM Workflow

```bash
python llm_workflow.py
```

Prompt Chaining

```bash
python prompt_chaining.py
```

Agentic AI

```bash
python agentic_ai.py
```

RAG

```bash
python rag.py
```

---

# Learning Outcomes

After completing this assignment, I learned how to:

- Use Large Language Models (LLMs)
- Build prompt chaining workflows
- Develop a simple AI agent
- Implement Retrieval-Augmented Generation (RAG)
- Integrate Ollama with Python

---

# Conclusion

This assignment successfully demonstrates the core concepts of Applied Agentic AI using local LLMs through Ollama. It covers LLM interaction, prompt engineering, AI agents, and retrieval-based question answering, providing a practical introduction to modern AI application development.
````

This README is suitable for submission with your assignment and clearly explains each component of the project.
