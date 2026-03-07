"""
structured_output.py

What it does: Forces Claude to return valid JSON, parsed and validated with Pydantic
Usage: python structured_output.py
Requirements: pip install anthropic pydantic

Set your API key: export ANTHROPIC_API_KEY="your-key-here"

Tip: Claude is highly reliable at structured JSON when you provide the schema
and use "Respond ONLY with valid JSON" in your prompt.

Contributed by: @yourusername
"""

import json
import os
from anthropic import Anthropic
from pydantic import BaseModel, ValidationError
from typing import Optional

client = Anthropic()


# --- Define your output schema with Pydantic ---

class ArticleSummary(BaseModel):
    title: str
    summary: str          # max 100 words
    sentiment: str        # "positive" | "neutral" | "negative"
    key_topics: list[str]
    reading_time_minutes: int
    recommended_audience: Optional[str] = None


# --- Prompt builder ---

def build_prompt(text: str, schema: type[BaseModel]) -> str:
    schema_json = json.dumps(schema.model_json_schema(), indent=2)
    return f"""Analyze the following text and respond ONLY with a valid JSON object.

IMPORTANT:
- Output raw JSON only — no markdown, no backticks, no explanation
- Follow the schema exactly
- Keep "summary" under 100 words
- "sentiment" must be exactly one of: "positive", "neutral", "negative"

Schema:
{schema_json}

Text to analyze:
{text}"""


# --- Main function ---

def analyze_article(text: str) -> ArticleSummary:
    prompt = build_prompt(text, ArticleSummary)

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.content[0].text.strip()

    # Strip accidental markdown fences if present
    if raw_output.startswith("```"):
        raw_output = raw_output.split("```")[1]
        if raw_output.startswith("json"):
            raw_output = raw_output[4:]
        raw_output = raw_output.strip()

    try:
        data = json.loads(raw_output)
        return ArticleSummary(**data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude returned invalid JSON: {e}\nRaw output:\n{raw_output}")
    except ValidationError as e:
        raise ValueError(f"JSON doesn't match schema: {e}\nRaw output:\n{raw_output}")


# --- Example usage ---

if __name__ == "__main__":
    sample_text = """
    Anthropic has released Claude 3.7 Sonnet, its most intelligent model yet. 
    The new model features extended thinking capabilities, allowing it to reason 
    through complex problems before responding. Early benchmarks show significant 
    improvements in coding, mathematics, and scientific reasoning tasks. Developers 
    can access the model through the API starting today, with pricing similar to 
    previous Sonnet models. The release marks a significant step in Anthropic's 
    mission to develop safe and beneficial AI systems.
    """

    result = analyze_article(sample_text)
    print("Parsed result:")
    print(result.model_dump_json(indent=2))
