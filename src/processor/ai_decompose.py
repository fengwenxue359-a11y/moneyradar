"""AI 拆解管线"""
import os
import logging
from src import config

logger = logging.getLogger(__name__)


class AIDecomposer:
    def __init__(self):
        from openai import OpenAI
        self.client = OpenAI(
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1"),
        )
        self.model = os.getenv("LLM_MODEL", "deepseek-chat")

    def decompose(self, item) -> str:
        prompt = config.DECOMPOSE_PROMPT.format(
            title=item.title,
            source=item.source,
            description=item.description,
            url=item.url,
        )
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一个专业的商业分析师，擅长将复杂的赚钱项目拆解为可执行的步骤。"},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=1500,
            )
            return resp.choices[0].message.content
        except Exception as e:
            logger.error(f"[AI拆解] 失败: {e}")
            return decompose_fallback(item)

    def decompose_batch(self, items: list, max_items: int = 8) -> list:
        results = []
        for item in items[:max_items]:
            logger.info(f"[AI拆解] 处理: {item.title[:50]}...")
            decomposition = self.decompose(item)
            results.append({"item": item, "decomposition": decomposition})
        return results


def decompose_fallback(item) -> str:
    return (
        f"**来源**：{item.source}\n\n"
        f"**描述**：{item.description}\n\n"
        f"**链接**：[{item.url}]({item.url})\n\n"
        f"**热度分**：{item.score:.1f}\n"
    )
