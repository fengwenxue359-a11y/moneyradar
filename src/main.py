"""MoneyRadar 主入口"""
import os
import sys
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, str(Path(__file__).parent.parent))

# 导入采集器和处理模块
from src.collectors.base import RawItem
from src.collectors.reddit_collector import RedditCollector
from src.collectors.github_collector import GitHubCollector
from src.collectors.rss_collector import RSSCollector
from src.collectors.duckduckgo_collector import DuckDuckGoCollector
from src.processor.dedup import deduplicate
from src.processor.scorer import score_items, filter_items
from src.processor.ai_decompose import AIDecomposer
from src.delivery.formatter import format_daily_report
from src.delivery.notifier import push_all

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("moneyradar.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("MoneyRadar")


def run():
    logger.info("=" * 50)
    logger.info("MoneyRadar 启动")
    logger.info("=" * 50)

    all_items = []
    
    # 1. 运行自动采集器
    collectors = [
        RedditCollector(),
        GitHubCollector(),
        RSSCollector(),
        DuckDuckGoCollector(),
    ]
    for collector in collectors:
        try:
            items = collector.collect()
            all_items.extend(items)
        except Exception as e:
            logger.error(f"[{collector.name}] 采集异常: {e}")

    # 2. 🌟 接入手动录入的国内平台情报
    from src import config
    for m in config.MANUAL_ITEMS:
        all_items.append(RawItem(
            title=m["title"],
            description=m["description"],
            url=m["url"],
            source=m["source"],
            score=100.0  # 强行给高分，让它排在最前面被优先拆解
        ))
        logger.info(f"[手动录入] 已加载: {m['title']}")

    logger.info(f"[采集] 总计 {len(all_items)} 条原始数据（含手动录入）")

    if not all_items:
        logger.warning("没有采集到任何数据，退出")
        return

    # 3. 去重、评分、筛选
    unique_items = deduplicate(all_items)
    scored_items = score_items(unique_items)
    top_items = filter_items(scored_items)

    # 如果筛选后数量不足，取前15名补足
    if len(top_items) < 5:
        top_items = scored_items[:15]
        logger.info(f"[筛选] 结果不足，取 Top {len(top_items)}")

    # 4. AI 拆解（每次最多拆解8个）
    decomposer = AIDecomposer()
    decompositions = decomposer.decompose_batch(top_items, max_items=8)

    # 5. 格式化日报
    today = datetime.now().strftime("%Y-%m-%d")
    report = format_daily_report(top_items, decompositions)

    # 6. 保存到本地 output 目录
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / f"{today}.md"
    output_file.write_text(report, encoding="utf-8")
    logger.info(f"[输出] 报告已保存: {output_file}")

    # 7. 推送到微信/Telegram
    push_all(
        title=f"赚钱雷达日报 {today}",
        content=report,
    )

    logger.info("=" * 50)
    logger.info("MoneyRadar 运行完成")
    logger.info("=" * 50)


if __name__ == "__main__":
    run()
