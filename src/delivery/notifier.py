"""推送通知模块"""
import os
import logging
import requests

logger = logging.getLogger(__name__)


def push_serverchan(title: str, content: str) -> bool:
    key = os.getenv("SERVERCHAN_KEY")
    if not key:
        return False
    try:
        resp = requests.post(
            f"https://sctapi.ftqq.com/{key}.send",
            data={"title": title[:32], "desp": content},
            timeout=15,
        )
        ok = resp.json().get("code") == 0
        logger.info(f"[Server酱] {'推送成功' if ok else '推送失败'}")
        return ok
    except Exception as e:
        logger.error(f"[Server酱] 推送异常: {e}")
        return False


def push_telegram(title: str, content: str) -> bool:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    try:
        text = f"*{title}*\n\n{content}"
        if len(text) > 4000:
            text = text[:4000] + "\n\n...（内容过长已截断，完整版见 GitHub）"

        resp = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "Markdown",
                "disable_web_page_preview": True,
            },
            timeout=15,
        )
        ok = resp.json().get("ok", False)
        logger.info(f"[Telegram] {'推送成功' if ok else '推送失败'}")
        return ok
    except Exception as e:
        logger.error(f"[Telegram] 推送异常: {e}")
        return False


def push_all(title: str, content: str):
    results = []
    results.append(push_serverchan(title, content))
    results.append(push_telegram(title, content))
    if not any(results):
        logger.warning("[推送] 所有通道均失败，请检查配置")
