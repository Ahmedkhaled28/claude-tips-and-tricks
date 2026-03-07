# 🧠 Claude Tips, Tricks & Hidden Features

<div align="center">

![Claude](https://img.shields.io/badge/Claude-Anthropic-orange?style=for-the-badge&logo=anthropic)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/yourusername/claude-tips-and-tricks?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/claude-tips-and-tricks?style=for-the-badge)

**A community-curated collection of tips, tricks, hidden features, prompt templates, and code snippets for getting the most out of Claude AI.**

[Tips & Tricks](#-tips--tricks) · [Prompts](#-prompt-library) · [Scripts](#-code-snippets--scripts) · [Contribute](#-contributing)

</div>

---

## 📖 Table of Contents

- [Why This Repo?](#-why-this-repo)
- [Tips & Tricks](#-tips--tricks)
  - [Prompting Fundamentals](#prompting-fundamentals)
  - [Hidden Features](#hidden-features)
  - [Context & Memory Tricks](#context--memory-tricks)
  - [Output Formatting](#output-formatting)
  - [Agentic & Tool Use](#agentic--tool-use)
  - [Claude.ai UI Tips](#claudeai-ui-tips)
- [Prompt Library](#-prompt-library)
  - [System Prompts](#system-prompts)
  - [Task Prompts](#task-prompts)
  - [Chain Prompts](#chain-prompts)
- [Code Snippets & Scripts](#-code-snippets--scripts)
- [Resources](#-resources)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Repo?

Claude is one of the most capable AI assistants available — but most people only scratch the surface of what it can do. This repo collects battle-tested tips, undocumented behaviors, clever prompting patterns, and reusable scripts from the community.

Whether you're a developer calling the API, a power user using Claude.ai, or a prompt engineer crafting complex workflows — there's something here for you.

---

## 🎯 Tips & Tricks

### Prompting Fundamentals

#### 1. Use XML Tags to Structure Complex Prompts
Claude is trained to understand XML-style tags natively. Use them to separate context, instructions, examples, and data clearly.

```
<context>
You are an expert data analyst at a SaaS company.
</context>

<task>
Analyze the following churn data and identify the top 3 risk segments.
</task>

<data>
{{paste your data here}}
</data>

<format>
Return a markdown table with: Segment | Risk Score | Recommended Action
</format>
```

**Why it works:** Claude was trained with XML-structured prompts and processes tagged sections with higher fidelity than plain paragraphs.

---

#### 2. Tell Claude What NOT to Do (Negative Constraints)
Positive instructions alone often leave too much room. Add explicit negative constraints.

```
Summarize this article.
- Do NOT use bullet points
- Do NOT include your own opinions
- Do NOT exceed 3 sentences
```

---

#### 3. Ask for Step-by-Step Reasoning Before the Answer
Trigger chain-of-thought by asking Claude to reason first.

```
Before answering, think through this step by step. 
Show your reasoning, then give your final answer.

Question: [your question]
```

---

#### 4. Use "Let's think about this carefully" for Hard Problems
This phrase consistently elicits more thorough, careful responses on complex topics compared to just asking the question directly.

---

#### 5. Specify Your Audience Explicitly
```
Explain quantum entanglement to:
- A 10-year-old
- A physics undergrad  
- A quantum computing researcher
```
Claude will adjust vocabulary, depth, and examples for each.

---

### Hidden Features

#### 6. Claude Can Hold Persona Across a Full Conversation
Set a system prompt (or opening message) once and Claude will maintain consistent behavior throughout:

```
You are Alex, a brutally honest senior software engineer with 20 years of experience. 
You give direct feedback without sugarcoating. You value simplicity over cleverness. 
You speak in short, punchy sentences.
```

---

#### 7. "Continue Exactly Where You Left Off"
When Claude's response gets cut off, use this exact phrase:

```
Continue exactly where you left off, starting from: "[last few words]"
```

This prevents Claude from summarizing or restarting.

---

#### 8. Force JSON Output with Schema
Claude will reliably output structured JSON when you provide the schema:

```
Respond ONLY with valid JSON. No explanation, no markdown, no preamble.

Schema:
{
  "title": "string",
  "summary": "string (max 100 words)",
  "sentiment": "positive | neutral | negative",
  "tags": ["string"]
}

Analyze the following text: {{text}}
```

---

#### 9. Use "The Magic Words" for Code
Adding these phrases dramatically improves code quality:
- `"Production-ready code only"`
- `"Include error handling"`
- `"Add inline comments explaining non-obvious logic"`
- `"Follow [language] best practices and idioms"`

---

#### 10. Instruct Claude to Ask Clarifying Questions First
```
Before you begin, ask me the 3-5 most important clarifying questions 
that would affect your approach. Wait for my answers before proceeding.
```

---

### Context & Memory Tricks

#### 11. Create a "User Profile" in Your System Prompt
```
## About the user
- Name: [name]
- Role: Senior backend engineer
- Stack: Python, FastAPI, PostgreSQL, Redis
- Prefers: Concise answers, code examples over prose, no hand-holding
- Never: Use bullet points for explanations
```

#### 12. Summarize and Carry Forward Long Conversations
When context is getting long, ask Claude to compress it:

```
Summarize everything we've discussed so far into a compact briefing 
I can paste at the start of a new conversation to continue seamlessly.
```

#### 13. Use Projects on Claude.ai for Persistent Context
Claude.ai Projects let you set a persistent system prompt and upload reference documents that persist across all chats in that project. Great for: codebases, style guides, research corpora.

---

### Output Formatting

#### 14. Request Specific Document Formats
```
Format your response as:
- A Notion-ready document with H1/H2/H3 headers
- A Slack message (no markdown, casual tone, < 300 chars)
- A formal memo with To/From/Date/Subject/Body
- An RFC document with Motivation, Proposal, Alternatives, and Drawbacks sections
```

#### 15. Control Response Length Precisely
- `"Answer in exactly 3 sentences."`
- `"Keep your response under 150 words."`
- `"Give me an exhaustive, comprehensive answer. Do not truncate."`

#### 16. Request Tables When Comparing Multiple Options
```
Compare these 5 database options across: Performance, Cost, Ease of Use, 
Scalability, and Community Support. Use a markdown table.
```

---

### Agentic & Tool Use

#### 17. Break Down Agentic Tasks with a Planning Step
```
I want you to [complex task]. 

First, create a detailed plan with numbered steps. 
Show me the plan and ask for my approval before executing anything.
```

#### 18. Use Sub-Agent Patterns for Parallel Work
When using Claude via API in agentic settings, orchestrate multiple specialized Claude instances:

```python
# See /scripts/python/parallel_subagents.py for full implementation
orchestrator = ClaudeOrchestrator()
results = await orchestrator.run_parallel([
    {"role": "researcher", "task": "Find competitor pricing"},
    {"role": "analyst",    "task": "Analyze our cost structure"},
    {"role": "writer",     "task": "Draft executive summary template"}
])
```

---

### Claude.ai UI Tips

#### 19. Keyboard Shortcuts
| Action | Shortcut |
|--------|----------|
| New chat | `Ctrl/Cmd + Shift + O` |
| Focus input | `Esc` then type |
| Submit message | `Enter` |
| New line in message | `Shift + Enter` |

#### 20. Use the Artifacts Panel for Iterative Work
When Claude generates code, documents, or visualizations as Artifacts, you can:
- Ask Claude to modify specific parts without rewriting the whole thing
- Download the artifact directly
- Share a link to the artifact (Claude.ai Pro)

#### 21. Upload Files for Context
Claude.ai supports uploading PDFs, images, CSVs, code files, and more. You can:
- Upload an entire codebase (as a ZIP or individual files)
- Reference uploaded docs with "As described in the uploaded document..."
- Upload screenshots for UI debugging

---

## 📚 Prompt Library

### System Prompts
Pre-built system prompts for common use cases. See [`/prompts/system-prompts/`](./prompts/system-prompts/)

| File | Description |
|------|-------------|
| [`senior-engineer.md`](./prompts/system-prompts/senior-engineer.md) | Code review & technical mentorship persona |
| [`research-analyst.md`](./prompts/system-prompts/research-analyst.md) | Deep research and synthesis |
| [`socratic-tutor.md`](./prompts/system-prompts/socratic-tutor.md) | Learn anything via Socratic dialogue |
| [`editor.md`](./prompts/system-prompts/editor.md) | Writing coach and copy editor |
| [`product-manager.md`](./prompts/system-prompts/product-manager.md) | PRD writing, user story generation |
| [`devils-advocate.md`](./prompts/system-prompts/devils-advocate.md) | Red team your ideas and decisions |

### Task Prompts
Single-shot prompts for specific tasks. See [`/prompts/task-prompts/`](./prompts/task-prompts/)

| File | Description |
|------|-------------|
| [`summarize-paper.md`](./prompts/task-prompts/summarize-paper.md) | Academic paper → structured summary |
| [`code-review.md`](./prompts/task-prompts/code-review.md) | Thorough code review with scoring |
| [`write-tests.md`](./prompts/task-prompts/write-tests.md) | Generate comprehensive test suites |
| [`explain-codebase.md`](./prompts/task-prompts/explain-codebase.md) | Onboard to a new codebase fast |
| [`rewrite-email.md`](./prompts/task-prompts/rewrite-email.md) | Polish emails for any tone/audience |
| [`sql-from-english.md`](./prompts/task-prompts/sql-from-english.md) | Natural language → SQL queries |

### Chain Prompts
Multi-step prompt sequences for complex workflows. See [`/prompts/chain-prompts/`](./prompts/chain-prompts/)

| File | Description |
|------|-------------|
| [`research-pipeline.md`](./prompts/chain-prompts/research-pipeline.md) | 5-step deep research workflow |
| [`blog-post-writer.md`](./prompts/chain-prompts/blog-post-writer.md) | Outline → draft → edit → SEO |
| [`system-design.md`](./prompts/chain-prompts/system-design.md) | Requirements → architecture → tradeoffs |

---

## 💻 Code Snippets & Scripts

### Python
| File | Description |
|------|-------------|
| [`basic_chat.py`](./scripts/python/basic_chat.py) | Minimal API chat loop |
| [`streaming_response.py`](./scripts/python/streaming_response.py) | Stream tokens as they generate |
| [`structured_output.py`](./scripts/python/structured_output.py) | Force JSON with Pydantic validation |
| [`parallel_subagents.py`](./scripts/python/parallel_subagents.py) | Run multiple Claude calls in parallel |
| [`conversation_manager.py`](./scripts/python/conversation_manager.py) | Multi-turn conversation with context trimming |
| [`batch_processor.py`](./scripts/python/batch_processor.py) | Process files/rows with Claude in bulk |

### JavaScript / TypeScript
| File | Description |
|------|-------------|
| [`basic_chat.js`](./scripts/javascript/basic_chat.js) | Node.js chat example |
| [`stream_to_ui.js`](./scripts/javascript/stream_to_ui.js) | Stream response to browser UI |
| [`tool_use.js`](./scripts/javascript/tool_use.js) | Function/tool calling example |

### Bash
| File | Description |
|------|-------------|
| [`claude_ask.sh`](./scripts/bash/claude_ask.sh) | One-liner CLI wrapper |
| [`summarize_file.sh`](./scripts/bash/summarize_file.sh) | Pipe any file to Claude for summary |

---

## 📡 Resources

### Official
- [Anthropic Docs](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/en/api)
- [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Claude Model Overview](https://docs.anthropic.com/en/docs/about-claude/models)

### Community
- [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) — Curated list of Claude Code tools
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — Production configs for Claude Code
- [claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide) — In-depth Claude Code guide

---

## 🤝 Contributing

Contributions are what make this repo valuable. Please read [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting.

**Quick contribution guide:**
1. Fork this repo
2. Create a branch: `git checkout -b tip/your-tip-name`
3. Add your content following the templates
4. Open a Pull Request

Every tip, prompt, and script should include:
- A clear title and description
- Why it works (the reasoning)
- A concrete example

---

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

<div align="center">

**If this helped you, please ⭐ the repo and share it with others!**

Made with ❤️ by the community, for the community.

</div>
