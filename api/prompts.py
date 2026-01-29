"""AI Prompts."""

# Specialized "Chain of Thought" and internal instructions are omitted.

PROMPTS = {
    "eli5": "Explain {topic} like I'm 5.",
    "eli10": "Explain {topic} like I'm 10.",
    "eli15": "Explain {topic} like I'm 15.",
    "eli20": "Explain {topic} for a college student.",
    "technical_depth": "Provide a deep technical analysis of {topic}."
}

TECHNICAL_DEPTH_PROMPT = """
Analyze the following topic in depth: {topic}
Context: {search_context}
Quote: {quote_text}
"""
