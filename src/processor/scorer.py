"""评分与筛选模块"""
import logging
from src import config

logger = logging.getLogger(__name__)


def score_items(items: list) -> list:
    for item in items:
        base_score = min(item.score / 1000.0, 10.0)
        text = f"{item.title} {item.description}".lower()
        action_bonus = sum(1 for kw in config.ACTIONABILITY_KEYWORDS if kw.lower() in text)
        item.score = base_score + action_bonus * 0.5

    items.sort(key=lambda x: x.score, reverse=True)
    return items


def filter_items(items: list, min_score: float = None) -> list:
    threshold = min_score or config.MIN_SCORE_TO_PUSH
    filtered = [i for i in items if i.score >= threshold]
    logger.info(f"[筛选] {len(items)} -> {len(filtered)} 条 (阈值 {threshold})")
    return filtered
