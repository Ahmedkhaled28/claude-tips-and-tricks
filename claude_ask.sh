#!/usr/bin/env bash
# claude_ask.sh
#
# What it does: One-liner CLI to ask Claude a question from the terminal
# Usage: ./claude_ask.sh "What is the capital of France?"
#        echo "Explain recursion" | ./claude_ask.sh
#        cat file.txt | ./claude_ask.sh "Summarize this"
#
# Requirements: curl, jq
#   Install jq: brew install jq  (macOS) or apt-get install jq (Linux)
#
# Set your API key: export ANTHROPIC_API_KEY="your-key-here"
# Or add to ~/.bashrc: export ANTHROPIC_API_KEY="your-key-here"
#
# Contributed by: @yourusername

set -e

# --- Config ---
MODEL="claude-sonnet-4-5"
MAX_TOKENS=2048

# --- Check dependencies ---
if ! command -v curl &>/dev/null; then
    echo "Error: curl is required. Install it and try again." >&2
    exit 1
fi

if ! command -v jq &>/dev/null; then
    echo "Error: jq is required. Install with: brew install jq (macOS) or apt-get install jq (Linux)" >&2
    exit 1
fi

# --- Check API key ---
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY is not set." >&2
    echo "Get your key at: https://console.anthropic.com/" >&2
    echo "Then run: export ANTHROPIC_API_KEY=\"your-key-here\"" >&2
    exit 1
fi

# --- Build prompt ---
# If piped input exists, combine it with CLI argument
if [ -p /dev/stdin ]; then
    PIPED_CONTENT=$(cat)
    QUESTION="${1:-Summarize this}"
    PROMPT="${QUESTION}

${PIPED_CONTENT}"
else
    PROMPT="${1}"
fi

if [ -z "$PROMPT" ]; then
    echo "Usage: $0 \"Your question here\""
    echo "       echo \"some text\" | $0 \"Summarize this\""
    exit 1
fi

# --- Make API request ---
RESPONSE=$(curl -s https://api.anthropic.com/v1/messages \
    -H "Content-Type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d "$(jq -n \
        --arg model "$MODEL" \
        --argjson max_tokens "$MAX_TOKENS" \
        --arg content "$PROMPT" \
        '{
            model: $model,
            max_tokens: $max_tokens,
            messages: [{ role: "user", content: $content }]
        }'
    )")

# --- Extract and print response ---
echo "$RESPONSE" | jq -r '.content[0].text // "Error: " + (.error.message // "Unknown error")'
