# Termloop

An AI term explainer for beginners. Enter a term like "RAG" and get a simple definition, an everyday analogy, an example and a quiz question.

| Folder | Stack |
| --- | --- |
| [`api/`](api/) | Python, FastAPI, LangChain agent |
| [`web/`](web/) | Next.js |

## Quick start

```bash
# API
cd api && uv sync
uv run app/main.py

# Web
cd web && npm install && npm run dev
```

## Prompt 1
Here's a reusable prompt. Replace the parts in brackets:

> Design [Product name], an AI [what it does] for [users].
Style: claymorphism, soft lavender base, violet primary, peach/mint/sunflower accents, rounded puffy cards, Bricolage Grotesque + Plus Jakarta Sans. Beginner-simple, no clutter, no emoji.
Screens: desktop main (interactive), phone main, phone progress.
Include: [core feature], streaming state, source badge, human-in-the-loop approval card, quiz with AI feedback, streaks, XP, credits, badges, safe-mode badge.
Clickable demo, sample data, accessible contrast.

For example, for a different product, the first line could be:

> Design Mathloop, an AI math step explainer for school students.

## Prompt 2

Here's a reusable prompt for the whole project. Replace the parts in brackets:

> Build [Termloop], an AI [term explainer] for [school students].
Stack: api/ = FastAPI + LangChain create_agent + SQLModel (SQLite), run with `uv run fastapi dev`. web/ = Next.js + Tailwind, claymorphism UI.
Check the latest LangChain docs first.
Agent: tools [glossary lookup from data/glossary.json] + safe web search (human-in-the-loop approval). Structured output: [simple, mental model + 3 steps, example, quiz]. Stream via SSE.
Quiz: LLM grades 0–3 with feedback.
Engagement: XP, levels, streaks, streak freeze, credits, daily goal, badges, history.
Guardrails: input/output filters, prompt injection, PII, school-safe, rate limit, tool/model call limits.
Tests with a fake model. Deliver a zip with README.
Start from my simple agent code (attached) and keep its style.

When you use it, attach your sample code (and glossary.json) with the message.
