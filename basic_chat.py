"""
basic_chat.py

What it does: Minimal multi-turn chat loop using the Claude API
Usage: python basic_chat.py
Requirements: pip install anthropic

Set your API key: export ANTHROPIC_API_KEY="your-key-here"

Contributed by: @yourusername
"""

import os
from anthropic import Anthropic

client = Anthropic()

# Optional: set a system prompt to customize Claude's behavior
SYSTEM_PROMPT = """You are a helpful assistant."""

def chat():
    conversation_history = []

    print("Claude Chat — type 'quit' to exit, 'clear' to reset conversation\n")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            conversation_history = []
            print("Conversation cleared.")
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=8096,
                system=SYSTEM_PROMPT,
                messages=conversation_history
            )

            assistant_message = response.content[0].text

            # Add assistant response to history for next turn
            conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            print(f"\nClaude: {assistant_message}")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Get your key at: https://console.anthropic.com/")
        exit(1)

    chat()
