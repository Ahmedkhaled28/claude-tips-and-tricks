---
title: "Comprehensive Code Review"
category: task-prompt
description: "Structured code review that scores quality and catches bugs, security issues, and style problems"
tested_on: claude-opus-4, claude-sonnet-4
contributed_by: "@yourusername"
---

# Comprehensive Code Review

## Purpose
Get a thorough, structured code review with severity levels and actionable fixes. Better signal-to-noise than asking "review my code."

## The Prompt

```
Review the following code. Structure your review exactly as follows:

## Overall Score: [X/10]
[One sentence verdict]

## Critical Issues (must fix before shipping)
For each: **Problem** → **Why it matters** → **Fix**

## Major Issues (should fix soon)
For each: **Problem** → **Why it matters** → **Fix**

## Minor Issues (good to address)
For each: **Problem** → **Suggested improvement**

## Security Checklist
- [ ] Input validation
- [ ] SQL injection risk
- [ ] Authentication/authorization
- [ ] Sensitive data exposure
- [ ] Error messages leaking info

## Performance Notes
Any O(n²) operations, unnecessary DB calls, memory concerns, etc.

## What's Done Well
2-3 specific things (not generic praise)

---
Language/Framework: [FILL IN]
Context: [FILL IN — e.g., "This is a REST API endpoint that handles user login"]

Code:
```[paste code here]```
```

## Usage Notes

- Always fill in Language/Framework and Context — it dramatically improves the review
- For large files, ask Claude to focus on a specific function or section first
- Combine with the Senior Engineer system prompt for even more direct feedback

## Customizations

```
# For frontend code, add:
## Accessibility Checklist
- [ ] ARIA labels
- [ ] Keyboard navigation
- [ ] Color contrast

# For API code, add:
## API Design
- [ ] RESTful conventions followed
- [ ] Consistent error response format
- [ ] Rate limiting considered
```
