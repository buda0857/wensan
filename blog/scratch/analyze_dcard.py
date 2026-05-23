import re
import os
import json
import jieba
from collections import Counter
from wordcloud import WordCloud

# Define file paths
input_file = r"d:\shu_drive\00_CC\blog\.firecrawl\dcard-talk.md"
output_json = r"d:\shu_drive\00_CC\blog\scratch\dcard_analysis.json"
output_image_dir = r"d:\shu_drive\00_CC\blog\assets"
output_wordcloud = os.path.join(output_image_dir, "dcard-wordcloud.png")

# Ensure directories exist
os.makedirs(output_image_dir, exist_ok=True)

# 1. Read scraped content
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 2. Parse posts
# The posts are formatted as:
# ## [Title](Link) or ## Title
# Followed by text content, and then reaction numbers.
post_blocks = content.split("\n## ")
posts = []

# Typical stopwords for Chinese NLP
stopwords = {
    "的", "了", "在", "是", "我", "你", "他", "她", "它", "就", "也", "都", "不", "有", "很", "而", "及",
    "與", "或", "等", "但", "和", "這", "那", "之", "於", "以", "嗎", "啦", "哈", "阿", "呢", "吧",
    "去", "被", "讓", "自己", "一個", "這個", "那個", "什麼", "如何", "如果", "看到", "覺得", "知道",
    "因為", "所以", "結果", "剛剛", "無聊", "網友", "好像", "應該", "還是", "不知道", "怎麼辦", "近期",
    "實在", "太多", "相關", "文章", "大家", "今天", "今天在", "我們", "目前", "請問", "因為我", "只是",
    "感覺", "覺得自己", "一樣", "其實", "真的", "超級", "看到這個", "出來", "看到有人", "看到網友",
    "有些", "有些事", "不會", "有些事再", "有些事再不", "有些事再不做", "去做", "去做嗎", "完之後",
    "而且", "而且有", "而且有9", "而且有9個", "而且有9個3", "而且有9個3天", "而且有9個3天以",
    "而且有9個3天以上", "開始", "開始認真", "開始認真考", "開始認真考慮", "考慮", "考慮牙",
    "考慮牙齒", "考慮牙齒矯", "考慮牙齒矯正", "牙齒矯正", "矯正", "諮詢", "諮詢一", "諮詢一輪",
    "諮詢一輪過", "諮詢一輪過後", "一輪過後", "過後", "過後好", "過後好像", "好像微",
    "好像微體", "好像微體會", "微體會", "體會要", "體會要多", "體會要多諮", "體會要多諮詢",
    "多諮詢", "多諮詢的", "多諮詢的意", "多諮詢的意義", "的意義", "意義", "前面", "前面幾",
    "前面幾間", "前面幾間諮", "前面幾間諮詢", "幾間諮詢", "諮詢都", "諮詢都是", "都是看",
    "都是看一下", "看一下", "看一下牙", "看一下牙齒", "一下牙齒", "牙齒", "然後", "然後就",
    "然後就開", "然後就開始", "就開始", "推薦", "推薦方", "推薦方案", "方案", "後來", "後來我",
    "後來我有", "我有遇", "我有遇到", "遇到一", "遇到一位", "一位醫", "一位醫師", "醫師", "是會",
    "是會...", "一個媽媽", "媽媽", "教兒子", "兒子", "課業", "講話", "講了", "很久", "至少", "持續",
    "小時", "有了", "寫了", "張紙條", "紙條", "討論室", "避免", "說話聲", "影響", "讀書", "環境",
    "一家人", "早上", "晚上", "回家", "東西", "全部", "環保局", "清運", "檢舉", "租屋處", "空間",
    "路中間", "消防通道", "傻眼", "是怎樣", "堆門口", "堆家門口", "放路", "放路中間", "擋消防",
    "擋消防通道", "什麼是", "什麼是生", "什麼是生物", "什麼是生物膜", "生物膜", "上禮拜", "同學",
    "一起", "宜蘭", "包棟", "過夜", "才發現", "發現居", "發現居然", "居然有", "居然有人",
    "有人不", "有人不知", "有人不知道", "生活", "常識", "生活常識", "簡單", "簡單講", "細菌",
    "聚集", "形成", "一層", "黏黏", "滑滑", "超常", "出現", "水槽", "排水口", "浴室", "磁磚",
    "蓮蓬頭", "洗手台", "長期", "大家最近", "最近也", "最近也開", "最近也開始", "也開始感",
    "也開始感受", "感受", "感受到", "感受到畢", "感受到畢業", "畢業", "畢業即", "畢業即失",
    "畢業即失業", "即失業", "失業了", "失業了嗎", "應屆", "應屆畢", "應屆畢業", "應屆畢業的",
    "找工作", "找工作了", "找工作了嗎", "投了", "好多", "好多家", "好多家職", "好多家職缺",
    "每一次", "一次按", "一次按出", "按出", "按出送", "按出送出", "送出", "送出履", "送出履歷",
    "履歷", "心裡", "心裡都", "心裡都抱", "抱著", "抱著一", "抱著一絲", "一絲期", "一絲期待",
    "期待", "換來", "換來的", "換來的只", "換來的只有", "只有無", "只有無止", "無止境",
    "無止境的", "無止境的已", "無止境的已讀", "已讀不", "已讀不回", "已讀不回。", "投遞",
    "狀態", "狀態從", "狀態從未", "狀態從未讀", "未讀變", "未讀變成", "變成已", "變成已讀",
    "然後就", "然後就再", "就再也", "就再也沒有", "沒有然", "沒有然後", "沒有然後了",
    "然後了", "那種", "那種付", "那種付出了", "付出了", "努力", "努力的", "一次", "兩次",
    "三天", "五天", "十分鐘", "五分鐘", "半夜", "零食", "零食櫃", "沒補貨", "只剩", "這包",
    "難吃", "難吃到", "必須", "說出來", "物理", "物理上", "物理上的", "物理上的難", "物理上的難開",
    "難開", "口感", "口感也", "口感也不", "也不好", "一點", "一點都", "一點都不", "一點都不像",
    "不像", "不像烤", "不像烤地", "不像烤地瓜", "烤地瓜", "蜜地瓜", "本土", "本土蜜", "本土蜜地",
    "本土蜜地瓜", "不香", "不香嗎", "前陣子", "一直", "唸想", "唸想吃", "唸想吃烤", "想吃烤地瓜",
    "時間", "基本", "超過", "床上", "可能", "野外", "姿勢", "速戰速決", "刺激", "享受", "野砲",
    "五分鐘其實", "不短", "外面", "發現", "慢慢", "另一半", "常在", "超過五分鐘", "換姿勢",
    "涉性侵", "強制", "猥褻", "成立", "強制性交", "強迫性交", "強制性交未遂", "性交未遂",
    "判刑", "兩年", "兩年六個月", "上訴", "期限", "屆滿", "檢察署", "決定", "不再提", "二審",
    "判決", "違背", "法令", "希望", "判決早日確定", "早日確定", "入監", "服刑", "一二審",
    "維持", "涉性侵猥褻", "一案成立", "上訴期限", "正式屆滿", "不再提上訴", "二審判決", "違背法令",
    "判決早日", "入監服刑", "直播", "野戰", "後續", "警局", "製作", "筆錄", "坦承", "影片",
    "男女", "主角", "男女主角", "一開始", "男方", "請假", "沒出現", "最後", "去了", "都說",
    "不知道現場", "現場", "攝影機", "會考", "中午", "考場", "開黃腔", "開黃", "打斷門牙",
    "門牙", "側門牙", "斷裂", "家屬", "氣憤", "報警", "警方", "指出", "少年", "已完成", "已完成筆錄",
    "函送", "少年法庭", "審理", "通報", "教育局", "啟動", "輔導", "機制", "輔導機制", "啟動輔導機制",
    "霸凌", "女同學", "霸凌女同學", "長期", "遭受", "同班", "男同學", "言語霸凌", "性騷擾",
    "考場開黃腔", "肚子", "一拳", "隨即", "反擊", "踢倒在地", "出拳", "毆打", "臉部", "三拳",
    "紅腫", "送肉粽", "朝聖", "畫面拍下來", "拍下來", "道士", "網路上", "網路上看", "網路上看到",
    "看到也算", "敬畏的心", "敬畏", "怕怕的", "連假", "全年", "放假日", "連休", "期待明年",
    "安排", "出國", "安排出國", "放假日121", "放假日121天", "連假出來", "期待明年了", "安排出國",
    "沒過一半", "已經開始", "期待", "期待明年", "安排", "出國", "安排出國", "連假出來了",
    "全年總放假日", "總放假日", "放假日121天", "而且有9個", "而且有9個3天", "而且有9個3天以上",
    "3天以上", "3天以上的連假", "以上的連假", "春節連休", "春節連休7天", "連休7天", "今年還沒",
    "今年還沒過一半", "還沒過一半", "已經開始期待", "開始期待明年", "期待明年了", "不說了",
    "不說了我要", "不說了我要先", "我要先來安排", "先來安排出國", "來安排出國", "（？"
}

# Positive and Negative lists for custom lexicon sentiment analysis
pos_words = ["恭喜", "讚", "爽", "期待", "賞心悅目", "好", "愛", "喜歡", "幸福", "健康", "富", 
             "提早退休", "雙贏", "精華", "好人", "友善", "進步", "笑", "高興", "開心", "美麗", 
             "有效", "有用", "安全", "成功", "自由", "支持", "好運", "輕鬆", "獲利", "治得好"]

neg_words = ["霸凌", "性騷擾", "開黃腔", "打斷", "門牙", "暴力", "車禍", "無照", "撞死", "死亡", 
             "違規", "罰單", "已讀不回", "已讀", "未讀", "失業", "歧視", "過世", "強迫", "性侵", 
             "強制", "猥褻", "難吃", "強迫症", "生病", "焦慮", "憂鬱", "恐慌", "出事", "險惡", 
             "落後", "失敗", "猴子", "難開", "垃圾", "有病", "痛苦", "難過", "氣憤", "受傷", 
             "紅腫", "斷裂", "爆汗", "嫌惡", "反對", "危險", "大吵", "沒錢", "養不起"]

all_text = ""
analyzed_posts = []

# Pinned posts extraction and general posts extraction
count = 0
for block in post_blocks:
    if not block.strip():
        continue
    
    # Extract title
    lines = [l.strip() for l in block.split("\n") if l.strip()]
    if not lines:
        continue
    
    title_line = lines[0]
    # Clean title
    title = title_line
    # If title has format [Title](Link), extract Title
    link_match = re.search(r"^\[(.*?)\]\((.*?)\)$", title_line)
    if link_match:
        title = link_match.group(1)
        link = link_match.group(2)
    else:
        link = ""
        # Try to find a link in the next few lines
        for line in lines[1:5]:
            m = re.search(r"https://www\.dcard\.tw/f/talk/p/\d+", line)
            if m:
                link = m.group(0)
                break
            m = re.search(r"\(https://www\.dcard\.tw/f/talk/p/\d+\)", line)
            if m:
                link = line.replace("(", "").replace(")", "").strip()
                break

    # Reconstruct clean text and extract snippet
    snippet = ""
    # Find snippet: usually the line after author/school or title that is a description
    content_lines = []
    for line in lines[1:]:
        # Skip reaction numbers, image links, author/time lines
        if re.search(r"^\d+$", line) or "megapx-assets" in line or "sticker-assets" in line or "link-meta" in line:
            continue
        if re.search(r"^[a-zA-Z\s]+\[\d+[h|d|m]\]", line) or re.search(r"^.*?\[\d+[h|d|m]\]", line):
            continue
        if line.startswith("!") or line.startswith("["):
            continue
        content_lines.append(line)
        
    if content_lines:
        snippet = " ".join(content_lines[:2])
    else:
        snippet = ""
        
    # Get interaction numbers (usually numbers at the end of the block)
    nums = [int(n) for n in lines if re.search(r"^\d+$", n)]
    likes = 0
    comments = 0
    
    # Clean likes and comments estimation from numbers
    if len(nums) >= 2:
        likes = nums[0]
        comments = nums[1]
    elif len(nums) == 1:
        likes = nums[0]

    # Combine text for NLP analysis
    full_text = title + " " + snippet
    all_text += " " + full_text
    
    # Sentiment calculation
    pos_score = sum(1 for w in pos_words if w in full_text)
    neg_score = sum(1 for w in neg_words if w in full_text)
    
    if pos_score > neg_score:
        sentiment = "Positive"
        sentiment_score = 0.5 + (pos_score - neg_score) * 0.1
    elif neg_score > pos_score:
        sentiment = "Negative"
        sentiment_score = 0.5 - (neg_score - pos_score) * 0.1
    else:
        sentiment = "Neutral"
        sentiment_score = 0.5
        
    sentiment_score = max(0.0, min(1.0, sentiment_score))
    
    # Add to list
    if not title.startswith("Products") and not title.startswith("Playground") and not title.startswith("Trending") and not title.startswith("Dcard") and not title.startswith("Forum") and not title.startswith("Terms"):
        count += 1
        posts.append({
            "id": count,
            "title": title,
            "snippet": snippet[:150] + "..." if len(snippet) > 150 else snippet,
            "link": link if link else "https://www.dcard.tw/f/talk",
            "likes": likes,
            "comments": comments,
            "sentiment": sentiment,
            "sentiment_score": round(sentiment_score, 2)
        })

# 3. Jieba Word Segmentation for WordCloud & Keyword Count
words = jieba.cut(all_text)
filtered_words = []
for word in words:
    word = word.strip()
    if len(word) >= 2 and word not in stopwords and not re.search(r"^[0-9a-zA-Z\s\.\#\-\/\!]+$", word):
        filtered_words.append(word)

word_counts = Counter(filtered_words)
top_keywords = [{"text": k, "value": v} for k, v in word_counts.most_common(50)]

# 4. Generate WordCloud Image
wordcloud_text = " ".join(filtered_words)
font_path = r"C:\Windows\Fonts\msjh.ttc"  # Microsoft JhengHei font for Chinese character rendering on Windows
if not os.path.exists(font_path):
    font_path = "arial"  # Fallback

wc = WordCloud(
    font_path=font_path,
    width=800,
    height=450,
    background_color="white",
    colormap="viridis",
    max_words=100
).generate(wordcloud_text)

wc.to_file(output_wordcloud)

# 5. Calculate overall metrics
sentiments = [p["sentiment"] for p in posts]
sentiment_counts = Counter(sentiments)

total_likes = sum(p["likes"] for p in posts)
total_comments = sum(p["comments"] for p in posts)

analysis_data = {
    "overall": {
        "total_posts": len(posts),
        "total_likes": total_likes,
        "total_comments": total_comments,
        "sentiment_distribution": {
            "Positive": sentiment_counts.get("Positive", 0),
            "Neutral": sentiment_counts.get("Neutral", 0),
            "Negative": sentiment_counts.get("Negative", 0)
        }
    },
    "top_keywords": top_keywords[:30],
    "posts": posts[:30]  # Exact top 30
}

# Write out JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(analysis_data, f, ensure_ascii=False, indent=2)

print("Analysis completed successfully!")
print(f"JSON saved to: {output_json}")
print(f"WordCloud image saved to: {output_wordcloud}")
