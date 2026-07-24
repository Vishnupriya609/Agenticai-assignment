from ollama import chat

# Get topic from user
topic = input("Enter a topic: ")

# ---------------- Step 1 ----------------
summary_response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Summarize the following topic in about 100 words:\n\n{topic}"
        }
    ]
)

summary = summary_response.message.content

print("\n========== SUMMARY ==========")
print(summary)

# ---------------- Step 2 ----------------
keypoints_response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Extract 5 key points from the following summary:\n\n{summary}"
        }
    ]
)

keypoints = keypoints_response.message.content

print("\n========== KEY POINTS ==========")
print(keypoints)

# ---------------- Step 3 ----------------
questions_response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Generate 3 interview questions based on the following summary:\n\n{summary}"
        }
    ]
)

questions = questions_response.message.content

print("\n========== QUESTIONS ==========")
print(questions)