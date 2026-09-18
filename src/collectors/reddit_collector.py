"""Reddit 采集器"""
import logging
from src.collectors.base import BaseCollector, RawItem
from src import config

logger = logging.getLogger(__name__)


class RedditCollector(BaseCollector):
    name = "Reddit"
    delay = 3.0

    def collect(self) -> list:
        items = []
        for sub in config.REDDIT_SUBS:
            url = f"https://www.reddit.com/r/{sub}/top.json"
            params = {"t": config.REDDIT_TIME_RANGE, "limit": config.REDDIT_TOP_LIMIT}
            resp = self.safe_get(url, params=params)
            if not resp:
                continue
            try:
                data = resp.json()
                for child in data.get("data", {}).get("children", []):
                    post = child["data"]
                    if post.get("ups", 0) < config.REDDIT_MIN_UPVOTES:
                        continue
                    items.append(RawItem(
                        title=post.get("title", ""),
                        description=post.get("selftext", "")[:800],
                        url=f"https://reddit.com{post.get('permalink', '')}",
                        source=f"r/{sub}",
                        score=post.get("ups", 0),
                        metadata={
                            "comments": post.get("num_comments", 0),
                            "created": post.get("created_utc", 0),
                        }
                    ))
            except Exception as e:
                logger.error(f"[Reddit] 解析 r/{sub} 失败: {e}")
            self._sleep()
        logger.info(f"[Reddit] 采集到 {len(items)} 条")
        return items
