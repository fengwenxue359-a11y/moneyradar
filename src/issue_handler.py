"""处理 GitHub Issue 触发的事件：自动 AI 拆解 + 评论回复 + 微信推送"""
import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.collectors.base import RawItem
from src.processor.ai_decompose import AIDecomposer
from src.delivery.notifier import push_all

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("IssueHandler")


def add_comment(issue_number: int, repo: str, token: str, body: str):
    """把 AI 拆解结果以评论形式发回 GitHub Issue"""
    import requests
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    resp = requests.post(url, headers=headers, json={"body": body}, timeout=15)
    if resp.status_code == 201:
        logger.info("[GitHub] 评论成功")
    else:
        logger.error(f"[GitHub] 评论失败: {resp.status_code} {resp.text}")


def run():
    logger.info("=" * 50)
    logger.info("Issue 拆解器启动")
    logger.info("=" * 50)

    title = os.getenv("ISSUE_TITLE", "未命名项目")
    body = os.getenv("ISSUE_BODY", "")
    issue_number = int(os.getenv("ISSUE_NUMBER", 0))
    repo = os.getenv("GITHUB_REPOSITORY", "")
    token = os.getenv("GITHUB_TOKEN", "")

    if not body.strip() and not title.strip():
        logger.warning("Issue 内容为空，退出")
        return

    item = RawItem(
        title=title,
        description=body[:2000],
        url=f"https://github.com/{repo}/issues/{issue_number}",
        source="Issue 手动录入",
        score=100.0,
    )
    logger.info(f"[Issue] 收到: {title}")

    decomposer = AIDecomposer()
    decomposition = decomposer.decompose(item)

    comment_body = (
        f"## 🤖 MoneyRadar AI 拆解结果\n\n"
        f"> 来源：Issue #{issue_number} · {title}\n\n"
        f"---\n\n"
        f"{decomposition}\n\n"
        f"---\n"
        f"*由 MoneyRadar 自动生成*"
    )

    add_comment(issue_number, repo, token, comment_body)

    push_all(
        title=f"💰 新项目拆解：{title[:30]}",
        content=comment_body,
    )

    logger.info("=" * 50)
    logger.info("Issue 拆解完成")
    logger.info("=" * 50)


if __name__ == "__main__":
    run()
