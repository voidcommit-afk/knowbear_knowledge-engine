"""Inference service."""

from typing import AsyncGenerator
from services.search import search_service

async def close_client():
    """Close any open clients."""
    pass

async def generate_stream_explanation(topic: str, level: str, **kwargs) -> AsyncGenerator[str, None]:
    """
    Stream explanation for topic.
    """
    yield f"Abstracted explanation for {topic}..."
    
    if kwargs.get("regenerate"):
        quote = await search_service.get_regeneration_quote()
        yield f"\n\n{quote}"
