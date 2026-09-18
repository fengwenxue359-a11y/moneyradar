"""DuckDuckGo 搜索采集器"""
import logging
from src.collectors.base import BaseCollector, RawItem
from src import config

logger = logging.getLogger(__name__)


class DuckDuckGoCollector(BaseCollector):
    name = "DuckDuckGo"
    delay = 3.0

    def collect(self) -> list:
        items = []
        for keyword in config.SEARCH_KEYWORDS:
            try:
                from ddgs import DDGS
                with DDGS() as ddgs:
                    results = list(ddgs.text(keyword, max_results=5))
                    for r in results:
                        items.append(RawItem(
                            title=r.get("title", ""),
                            description=r.get("body", "")[:500],
                            url=r.get("href", ""),
                            source="DuckDuckGo",
                            score=0,
                            metadata={"keyword": keyword},
                        ))
            except ImportError:
                logger.warning("[DuckDuckGo] 未安装 ddgs 库，跳过")
                break
            except Exception as e:
                logger.error(f"[DuckDuckGo] 搜索 '{keyword}' 失败: {e}")
            self._sleep()
        logger.info(f"[DuckDuckGo] 采集到 {len(items)} 条")
        return items
