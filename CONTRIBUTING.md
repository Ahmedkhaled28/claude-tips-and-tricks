# Contributing to Claude Tips, Tricks & Hidden Features

First off — thank you! This repo lives and grows through community contributions. Every tip, prompt, and script that gets added makes this more useful for everyone.

---

## 📋 What Can I Contribute?

| Type | Location | What We're Looking For |
|------|----------|----------------------|
| Tips & Tricks | `README.md` | Prompting techniques, behavioral insights, UI tricks |
| System Prompts | `prompts/system-prompts/` | Reusable personas for Claude |
| Task Prompts | `prompts/task-prompts/` | Single-purpose, copy-paste prompts |
| Chain Prompts | `prompts/chain-prompts/` | Multi-step, sequential prompt workflows |
| Python scripts | `scripts/python/` | API usage patterns, utilities |
| JS/TS scripts | `scripts/javascript/` | Frontend/Node API patterns |
| Bash scripts | `scripts/bash/` | CLI tools and shell helpers |

---

## ✅ Contribution Standards

### For Tips & Tricks

Every tip should follow this format:

```markdown
#### [Number]. [Title — Clear and Action-Oriented]

[1-2 sentence explanation of what this is]

```
[Example prompt or code]
```

**Why it works:** [The reasoning — what behavior or training insight explains this]
```

**Good tip criteria:**
- Verified to work (tested it yourself)
- Explains *why* it works, not just *what* to do
- Includes a concrete, copy-pasteable example
- Adds something not already covered in the README

---

### For Prompt Files

All prompt files should include a frontmatter header:

```markdown
---
title: "Your Prompt Title"
category: system-prompt | task-prompt | chain-prompt
description: "One sentence: what does this prompt do?"
tested_on: claude-opus-4, claude-sonnet-4  
contributed_by: "@yourgithubhandle"
---

# [Prompt Title]

## Purpose
[What problem does this solve?]

## The Prompt

```
[Your prompt here]
```

## Usage Notes
[Any tips, caveats, or customization guidance]

## Example Output
[Optional but encouraged: show what a good result looks like]
```

---

### For Code Scripts

All scripts should include:
- A header comment explaining what it does
- Clear variable names
- Inline comments for non-obvious logic
- Error handling
- A `README` note if setup is required (API keys, deps, etc.)

```python
"""
brief_script_name.py

What it does: [one line]
Usage: python brief_script_name.py
Requirements: anthropic>=0.20.0

Contributed by: @yourgithubhandle
"""
```

---

## 🔀 How to Submit

### Option A — Pull Request (Preferred)

1. **Fork** this repository
2. **Create a branch** with a descriptive name:
   ```bash
   git checkout -b tip/xml-structured-prompts
   git checkout -b prompt/senior-engineer-persona
   git checkout -b script/streaming-cli-tool
   ```
3. **Make your changes** following the standards above
4. **Commit** with a clear message:
   ```bash
   git commit -m "feat: add tip for XML-structured prompting"
   git commit -m "prompt: add senior engineer system prompt"
   git commit -m "script: add Python streaming example"
   ```
5. **Open a Pull Request** using the PR template

### Option B — Open an Issue

Not comfortable with PRs? [Open an issue](../../issues/new/choose) using the "New Tip" or "New Prompt" template and describe your contribution. A maintainer will add it.

---

## ❌ What We Don't Accept

- Tips that promote jailbreaking or bypassing Claude's guidelines
- Prompts designed to produce harmful, deceptive, or misleading content
- Duplicate tips (search before submitting)
- Vague tips without examples ("just be more specific" without showing how)
- Scripts with hardcoded API keys

---

## 🔍 Review Process

1. A maintainer reviews your PR within **3-5 business days**
2. We may ask for revisions (clearer example, better explanation, etc.)
3. Once approved, your contribution is merged and you're added to the contributors list

---

## 🙋 Questions?

Open a [discussion](../../discussions) and we'll help you out.

---

Thank you for making this resource better for everyone! 🙏
