---
title: "5-Step Deep Research Pipeline"
category: chain-prompt
description: "Sequential prompts to go from a vague topic to a polished research report"
tested_on: claude-opus-4
contributed_by: "@yourusername"
---

# 5-Step Deep Research Pipeline

## Purpose
A multi-turn prompt chain that systematically transforms a topic into a thorough, structured research output. Each step builds on the previous one.

---

## Step 1 — Scope & Question Framing

```
I want to research: [YOUR TOPIC]

Before we start, help me frame this research properly:
1. What are the 3 most important sub-questions I should answer?
2. What are the key tensions or debates in this space?
3. What assumptions am I likely making that I should examine?
4. What's out of scope (to keep this focused)?

Output as a structured research brief I can refer back to.
```

---

## Step 2 — Knowledge Landscape

```
Based on the research brief above, give me a comprehensive overview of what is 
currently known about [TOPIC].

Structure it as:
- **Established consensus** (things experts agree on)
- **Active debates** (things still contested)
- **Known unknowns** (important gaps in knowledge)
- **Recent developments** (last 2-3 years)

Be specific. Cite named researchers, papers, companies, or events where relevant.
```

---

## Step 3 — Deep Dive on Key Question

```
Let's go deep on [pick one sub-question from Step 1].

I want:
1. The strongest case FOR [position A]
2. The strongest case FOR [position B]  
3. What evidence would help resolve this?
4. Your assessment of the current state of evidence

Steel-man both sides before giving any assessment.
```

---

## Step 4 — Implications & So What

```
Given everything we've covered, help me think through implications.

For each of the following audiences, what are the 2-3 most important 
actionable implications from this research?

- [Audience 1, e.g., "a startup founder in this space"]
- [Audience 2, e.g., "a policy maker"]
- [Audience 3, e.g., "an individual consumer"]

Be specific about what they should do differently based on this research.
```

---

## Step 5 — Final Report Generation

```
Now synthesize everything into a final research report.

Format:
# [Title]

## Executive Summary (3-4 sentences)

## Background & Context

## Key Findings
### Finding 1: [Title]
### Finding 2: [Title]
### Finding 3: [Title]

## Implications

## Open Questions & Future Research

## Sources & Further Reading
(List any specific sources, papers, or people mentioned in our conversation)

---

Make it suitable for sharing with a professional audience. 
Use concrete examples and specific evidence, not vague generalizations.
```

---

## Usage Notes

- Best run in a **single conversation** so each step has context from previous steps
- Works best with Claude Opus for the depth of reasoning
- For step 3, you can run it multiple times for different sub-questions
- If you have web search enabled, tell Claude: "Use web search to ground your findings in current sources"
