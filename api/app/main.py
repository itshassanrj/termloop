import json
from pathlib import Path

from langchain.agents import create_agent
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent.parent
GLOSSARY_FILE = BASE_DIR / "data" / "glossary.json"

def load_glossary() -> dict:
    with open(GLOSSARY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {k.lower(): v for k, v in data.items()}

GLOSSARY = load_glossary()


class TermExplanation(BaseModel):
    term: str = Field(description="The AI term being explained")
    simple: str = Field(description="One easy sentence a beginner understands")
    mental_model: str = Field(
        description="An everyday analogy that makes the idea click, "
        "e.g. 'RAG is like an open-book exam'"
    )
    example: str = Field(description="One real-life example")
    quiz: str = Field(description="One short question to test the learner")
    from_glossary: bool = Field(description="True if the definition came from the glossary")

# Agent tool
def lookup_term(term: str) -> str:
    """Look up an AI term in the glossary. Use this first for every term."""
    return GLOSSARY.get(term.strip().lower(), "NOT_FOUND")

# System prompt
SYSTEM = """You are an AI Term Explainer for beginners.
Always call lookup_term first.
If found, base your answer on that definition and set from_glossary = true.
If NOT_FOUND, explain from your own knowledge and set from_glossary = false.
For mental_model, use a simple everyday comparison (school, kitchen, shop, phone), not technical words.
Keep every field short and simple."""

# AI agent
agent = create_agent(
    model="ollama:qwen3.5:4b",
    tools=[lookup_term],
    system_prompt=SYSTEM,
    response_format=TermExplanation,
)

q = input("Term: ").strip()
result = agent.invoke(
    {"messages": [{"role": "user", "content": q}]}
)
ans = result["structured_response"]

print(f"\nTerm: {ans.term}")
print(f"Simple: {ans.simple}")
print(f"Mental model: {ans.mental_model}")
print(f"Example: {ans.example}")
print(f"Quiz: {ans.quiz}")
print(f"Source: {'AI glossary' if ans.from_glossary else 'LLM knowledge'}")
