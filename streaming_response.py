"""
streaming_response.py

What it does: Streams Claude's response token-by-token as it generates
Usage: python streaming_response.py
Requirements: pip install anthropic

Why stream? Streaming dramatically improves perceived response time for users.
Instead of waiting 10s for a full response, they see output start in <1s.

Contributed by: @yourusername
"""

import os
import sys
import time
from anthropic import Anthropic

client = Anthropic()


def stream_response(prompt: str, system: str = "") -> str:
    """
    Stream Claude's response, printing each token as it arrives.
    Returns the complete response text when done.
    """
    full_response = []
    start_time = time.time()

    kwargs = {
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        kwargs["system"] = system

    with client.messages.stream(**kwargs) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response.append(text)

    elapsed = time.time() - start_time
    complete = "".join(full_response)

    # Print usage stats
    final = stream.get_final_message()
    input_tokens = final.usage.input_tokens
    output_tokens = final.usage.output_tokens

    print(f"\n\n{'─' * 50}")
    print(f"⏱  {elapsed:.1f}s  |  📥 {input_tokens} tokens in  |  📤 {output_tokens} tokens out")

    return complete


# --- Example usage ---

if __name__ == "__main__":
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Write a haiku about streaming APIs."

    print(f"Prompt: {prompt}\n{'─' * 50}\n")
    stream_response(prompt)
