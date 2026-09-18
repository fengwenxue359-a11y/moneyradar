"""日报格式化"""
from datetime import datetime


def format_daily_report(scored_items: list, decompositions: list) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        f"# 赚钱雷达日报 — {today}",
        "",
        f"> 今日共采集到 **{len(scored_items)}** 条信号，精选 **{len(decompositions)}** 条深度拆解",
        "",
        "---",
        "",
    ]

    lines.append("## 今日速览")
    lines.append("")
    for i, item in enumerate(scored_items[:15], 1):
        score_str = f"⭐{item.score:.1f}" if item.score > 0 else ""
        lines.append(f"{i}. **[{item.title}]({item.url})** — {item.source} {score_str}")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## 深度拆解")
    lines.append("")
    for i, d in enumerate(decompositions, 1):
        item = d["item"]
        lines.append(f"### {i}. {item.title[:60]}")
        lines.append(f"> 来源：{item.source} | [原文链接]({item.url})")
        lines.append("")
        lines.append(d["decomposition"])
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append(f"*由 MoneyRadar 自动生成 · {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    return "\n".join(lines)
