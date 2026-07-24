from ollama import chat

# Accept user input
user_input = input("Enter your question: ")

# Send input to Ollama LLM
response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)

# Display response
print("\nLLM Response:\n")
print(response.message.content)