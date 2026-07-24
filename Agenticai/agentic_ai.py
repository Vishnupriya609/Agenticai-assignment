from ollama import chat

# Get task from the user
task = input("Enter your task: ")

# ---------------- PLAN ----------------
plan_response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
You are an AI agent.

Task:
{task}

Create a clear step-by-step plan to complete this task.
"""
        }
    ]
)

plan = plan_response.message.content

print("\n========== PLAN ==========\n")
print(plan)

# ---------------- EXECUTE ----------------
execution_response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"""
Execute the following plan and provide the final result.

Plan:
{plan}
"""
        }
    ]
)

result = execution_response.message.content

print("\n========== FINAL OUTPUT ==========\n")
print(result)