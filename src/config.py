"""全局配置：信源、关键词、评分规则"""

# ========== 采集信源 ==========
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

SEARCH_KEYWORDS = [
    "知识付费 赚钱项目 一人",
    "小红书 虚拟资料 变现",
    "抖音 AI 副业 可执行",
    "TikTok digital product passive income",
    "YouTube course launch no camera",
    "闲鱼 虚拟资料 选品",
    "AI side hustle 2026",
    "抖音 知识付费 课程 拆解",
    "闲鱼 虚拟资料 月入",
    "TikTok 中文教学 出海",
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

# ========== AI 拆解提示词 ==========
DECOMPOSE_PROMPT = """你是一个商业项目分析师。请对以下项目信息进行结构化拆解。

原始信息：
标题：{title}
来源：{source}
描述：{description}
链接：{url}

请严格按以下格式输出（不要添加额外内容）：

## 项目名称
（一句话概括）

## 核心逻辑
（这个项目靠什么赚钱，2-3句话）

## 启动成本
（金钱成本和时间成本，具体数字）

## 执行步骤
1. （第一步具体做什么）
2. （第二步）
3. （第三步）

## 收入模式
（怎么收费、客单价范围、预估月收入）

## 单人可执行
（是/否，如果否请说明需要什么资源）

## 第一周行动清单
（如果今天开始，第一周可以做的3件具体的事）

## 风险点
（可能失败的原因）
"""
