"""去重模块"""
import hashlib
import logging

logger = logging.getLogger(__name__)


def deduplicate(items: list) -> list:
    seen = set()
    unique = []
    for item in items:
        normalized = item.title.strip().lower()
        key = hashlib.md5(normalized.encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            unique.append(item)
    logger.info(f"[去重] {len(items)} -> {len(unique)} 条")
    return unique
