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

# ========== 🎯 针对国内平台的 AI 拆解提示词 ==========
DECOMPOSE_PROMPT = """你是一个国内自媒体商业分析师。请对以下国内平台（抖音/小红书/闲鱼）的项目信息进行结构化拆解。

原始信息：
标题：{title}
来源：{source}
描述：{description}
链接：{url}

请严格按以下格式输出（不要添加额外内容）：

## 项目名称
（一句话概括）

## 核心逻辑
（靠什么赚钱，国内用户为什么买单，2-3句话）

## 启动成本
（具体到金钱和时间，例如：0元，每天2小时）

## 执行步骤
1. （第一步具体做什么）
2. （第二步）
3. （第三步）

## 收入模式
（客单价、变现路径、预估月收入）

## 单人可执行
（是/否，如果否需要什么资源）

## 第一周行动清单
（如果今天开始，第一周可以做的3件具体的事）

## 避坑指南
（国内平台特有的违规风险、退款率、封号风险等）
"""
