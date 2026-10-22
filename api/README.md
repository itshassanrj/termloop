# Termloop - API

A LangChain agent that explains AI terms. It checks `data/glossary.json` first and uses the model's own knowledge when the term is not there.

## Setup

Requires Python 3.13, [uv](https://docs.astral.sh/uv/) and [Ollama](https://ollama.com) with `qwen3.5:4b` pulled.

```bash
cp .env.example .env
uv sync
uv run python app/main.py
```

## Output

Each answer has: `term`, `simple`, `mental_model`, `example`, `quiz`, `from_glossary`.

Add terms by editing `data/glossary.json`.
