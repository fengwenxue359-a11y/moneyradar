"""GitHub 采集器"""
import logging
from src.collectors.base import BaseCollector, RawItem
from src import config

logger = logging.getLogger(__name__)


class GitHubCollector(BaseCollector):
    name = "GitHub"
    delay = 2.0

    def collect(self) -> list:
        items = []
        headers = {
            "User-Agent": "MoneyRadar/1.0",
            "Accept": "application/vnd.github.v3+json",
        }
        for query in config.GITHUB_QUERIES:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": f"{query} in:name,description,readme",
                "sort": "stars",
                "order": "desc",
                "per_page": 5,
            }
            resp = self.safe_get(url, headers=headers, params=params)
            if not resp:
                continue
            try:
                data = resp.json()
                for repo in data.get("items", []):
                    if repo.get("stargazers_count", 0) < config.GITHUB_MIN_STARS:
                        continue
                    items.append(RawItem(
                        title=repo.get("full_name", ""),
                        description=repo.get("description", "") or "",
                        url=repo.get("html_url", ""),
                        source="GitHub",
                        score=repo.get("stargazers_count", 0),
                        metadata={
                            "language": repo.get("language", ""),
                            "updated": repo.get("updated_at", ""),
                        }
                    ))
            except Exception as e:
                logger.error(f"[GitHub] 搜索 '{query}' 失败: {e}")
            self._sleep()
        logger.info(f"[GitHub] 采集到 {len(items)} 条")
        return items
