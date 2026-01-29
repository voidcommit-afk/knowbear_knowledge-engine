"""Redis caching service."""

import orjson
from typing import Any
try:
    import redis.asyncio as redis
except ImportError:
    # Fallback for environments without redis
    redis = None

from config import get_settings
from logging_config import logger

_client = None

async def get_redis():
    """Get or create Redis client."""
    global _client
    if _client is None:
        settings = get_settings()
        # Generic Redis connection logic
        # In production, replace with your Redis URL
        url = settings.redis_url or "redis://localhost:6379"
        
        if redis:
            _client = redis.from_url(
                url, 
                decode_responses=False,
                socket_timeout=2.0,
                socket_connect_timeout=2.0
            )
    return _client

async def cache_get(key: str) -> dict[str, Any] | None:
    """Get cached value."""
    try:
        r = await get_redis()
        if not r: return None
        val = await r.get(key)
        return orjson.loads(val) if val else None
    except Exception as e:
        logger.warning("cache_get_failed", key=key, error=str(e))
        return None

async def cache_set(key: str, value: dict[str, Any], ttl: int | None = None) -> bool:
    """Set cached value with TTL."""
    try:
        r = await get_redis()
        if not r: return False
        settings = get_settings()
        await r.setex(key, ttl or settings.cache_ttl, orjson.dumps(value))
        return True
    except Exception as e:
        logger.error("cache_set_failed", key=key, error=str(e))
        return False

async def close_redis() -> None:
    """Close Redis connection."""
    global _client
    if _client:
        await _client.close()
        _client = None
