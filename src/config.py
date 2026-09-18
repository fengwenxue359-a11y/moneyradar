"""全局配置：信源、关键词、评分规则、手动录入"""

# ========== 海外采集信源（保留基础盘） ==========
REDDIT_SUBS = [
    "WorkOnline", "Beermoney", "Passive_Income",
    "Entrepreneur", "sidehustle", "juststart",
]

REDDIT_TOP_LIMIT = 10
REDDIT_MIN_UPVOTES = 50
REDDIT_TIME_RANGE = "day"

GITHUB_QUERIES = [
    "ai money maker",
    "ai side hustle",
    "passive income tool",
    "content automation",
    "make money online",
]
GITHUB_MIN_STARS = 5

RSS_FEEDS = [
    "https://www.reddit.com/r/WorkOnline/.rss",
    "https://www.reddit.com/r/Beermoney/.rss",
    "https://www.reddit.com/r/sidehustle/.rss",
    "https://www.reddit.com/r/juststart/.rss",
    "https://www.producthunt.com/feed",
]

# ========== 搜索引擎关键词（重点是国内平台） ==========
SEARCH_KEYWORDS = [
    "抖音 赚钱博主 项目拆解",
    "小红书 虚拟资料 变现 复盘",
    "闲鱼 卖教程 赚钱 案例",
    "知识付费 博主 月入 拆解",
    "公众号 一人公司 副业 项目",
    "TikTok 中文 教学 独立站",
    "AI 自媒体 副业 实操",
    "抖音 小程序 推广 赚钱"
]

# ========== 🌟 手动录入区（每天你自己填这里） ==========
MANUAL_ITEMS = [
    # 复制下面的格式，增加你看到的国内赚钱博主
    {
        "title": "抖音博主：AI生成职场PPT",
        "description": "博主演示用AI生成PPT，评论区全是扣1要教程的，主页挂了9.9元的小程序，销量显示3000+",
        "url": "https://www.douyin.com/user/xxxx",
        "source": "手动录入-抖音"
    },
    {
        "title": "小红书卖幼小衔接资料",
        "description": "客单价29.9，笔记就是几张图展示资料内容，评论区引导私信，店里卖了6000多单",
        "url": "https://www.xiaohongshu.com/user/xxxx",
        "source": "手动录入-小红书"
    }
]

# ========== 评分规则 ==========
SCORE_WEIGHTS = {
    "upvotes": 0.3,
    "comments": 0.2,
    "recency": 0.2,
    "actionability": 0.3,
}

ACTIONABILITY_KEYWORDS = [
    "step by step", "how to", "guide", "tutorial", "template",
    "checklist", "roadmap", "starter", "executable",
    "教程", "步骤", "拆解", "模板", "可执行", "落地",
]

# ========== 推送配置 ==========
DAILY_PUSH_HOUR = 8
MIN_SCORE_TO_PUSH = 5.0

# ========== 🎯 针对国内平台、直接落地的 AI 拆解提示词 ==========
DECOMPOSE_PROMPT = """你是一个实战派的国内自媒体落地教练。你的任务不是分析一个项目，而是告诉一个普通人：如何在一个月内，从零开始模仿这个博主，赚到第一笔钱。

原始信息：
标题：{title}
来源：{source}
描述：{description}
链接：{url}

请严格按以下格式输出，越具体越好，不要讲大道理：

## 一句话总结他靠什么赚钱
（说人话，不要术语）

## 他的变现漏斗拆解
- 引流品（免费内容）：他发什么吸引人？
- 信任品（低价）：他卖什么让人第一次掏钱？价格多少？
- 利润品（高价）：他最终靠什么赚大钱？价格多少？

## 他做对了哪三件事
（普通人最容易忽略，但他做得特别好的地方）

## 我能抄什么（重点！）
请列出 5 条可以直接照抄的动作，每条都要具体到：
- 抄什么（具体形式，比如：用手机拍60秒口播视频）
- 用什么工具（具体工具名，如剪映、DeepSeek、Canva）
- 抄的难度（1-5星）
- 预计第一次能出什么结果（比如：发3条测试视频）

## 我不该抄什么
（哪些资源是他独有的，普通人抄不了，比如：他有北师大背景、他有团队）

## 第一周傻瓜式行动清单
请按 Day 1 到 Day 7 写，每天只做一件事，要具体到动作：
- Day 1：（具体动作）
- Day 2：（具体动作）
- Day 3：（具体动作）
- Day 4：（具体动作）
- Day 5：（具体动作）
- Day 6：（具体动作）
- Day 7：（具体动作）

## 起步需要花多少钱
（如果超过100元，请说明哪里可以省掉）

## 最可能死在哪一步
（说人话，比如：可能发了10条笔记都没人看，你要怎么处理）

## 立即行动
（如果用户现在放下手机，今晚就能做的第一件事是什么？）"""
