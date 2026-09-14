import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("DEEPSEEK_API_KEY is missing from your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

messages = [
    {
        "role": "system",
        "content": """
You are Nexus, a friendly AI companion.

You are intelligent, curious, conversational, and helpful.
Talk naturally rather than sounding like a formal assistant.

Help the user learn, think, explore ideas, and have interesting conversations.
When you don't know something, be honest.
"""
    }
]

print("=" * 50)
print("             NEXUS AI COMPANION")
print("=" * 50)
print("Type 'exit' to quit.")
print()

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Nexus: See you later.")
        break

    if not user_input.strip():
        continue

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7
        )

        answer = response.choices[0].message.content

        print(f"\nNexus: {answer}\n")

        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print(f"\nError: {e}\n")
