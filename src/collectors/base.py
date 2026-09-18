"""采集器基类"""
import time
import logging
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class RawItem:
    title: str
    description: str
    url: str
    source: str
    score: float = 0.0
    metadata: dict = field(default_factory=dict)


class BaseCollector:
    name: str = "base"
    delay: float = 2.0

    def collect(self) -> list:
        raise NotImplementedError

    def _sleep(self):
        time.sleep(self.delay)

    def safe_get(self, url, headers=None, params=None, timeout=15):
        import requests
        headers = headers or {"User-Agent": "MoneyRadar/1.0"}
        for attempt in range(3):
            try:
                resp = requests.get(url, headers=headers, params=params, timeout=timeout)
                resp.raise_for_status()
                return resp
            except Exception as e:
                logger.warning(f"[{self.name}] 请求失败 (attempt {attempt+1}/3): {e}")
                time.sleep(self.delay * (attempt + 1))
        return None
