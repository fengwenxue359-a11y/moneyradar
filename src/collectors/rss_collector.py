"""RSS 采集器"""
import logging
from src.collectors.base import BaseCollector, RawItem
from src import config

logger = logging.getLogger(__name__)


class RSSCollector(BaseCollector):
    name = "RSS"
    delay = 2.0

    def collect(self) -> list:
        import feedparser
        items = []
        for feed_url in config.RSS_FEEDS:
            try:
                feed = feedparser.parse(feed_url)
                for entry in feed.entries[:10]:
                    items.append(RawItem(
                        title=entry.get("title", ""),
                        description=entry.get("summary", "")[:500],
                        url=entry.get("link", ""),
                        source=f"RSS: {feed.feed.get('title', feed_url)[:30]}",
                        score=0,
                        metadata={"published": entry.get("published", "")},
                    ))
            except Exception as e:
                logger.error(f"[RSS] 解析 {feed_url} 失败: {e}")
            self._sleep()
        logger.info(f"[RSS] 采集到 {len(items)} 条")
        return items
