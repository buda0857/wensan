import requests
from bs4 import BeautifulSoup
import re
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import time
import os
from collections import Counter

# Set up matplotlib for Chinese characters
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # For Windows
plt.rcParams['axes.unicode_minus'] = False

# Download stopwords or set basic stopwords (just a simple list for this demo)
STOPWORDS = set(["的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "一個", "上", "也", "很", "到", "說", "要", "去", "你", "會", "著", "沒有", "看", "好", "自己", "這", "那"])

def get_page_articles(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    cookies = {'over18': '1'}
    try:
        r = requests.get(url, headers=headers, cookies=cookies, timeout=5)
    except:
        return [], None
    soup = BeautifulSoup(r.text, 'html.parser')
    
    articles = []
    divs = soup.find_all("div", class_="r-ent")
    for d in divs:
        if d.find("a"):
            title = d.find("a").text
            href = "https://www.ptt.cc" + d.find("a")['href']
            # Find category type like [食記]
            match = re.search(r'\[(.*?)\]', title)
            article_type = match.group(1) if match else "其他"
            articles.append({
                "title": title,
                "url": href,
                "type": article_type
            })
            
    # Find previous page link
    paging = soup.find("div", class_="btn-group btn-group-paging")
    if paging:
        prev_link = paging.find_all("a")[1]
        if 'href' in prev_link.attrs:
            return articles, "https://www.ptt.cc" + prev_link['href']
    return articles, None

def get_article_content(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    cookies = {'over18': '1'}
    try:
        r = requests.get(url, headers=headers, cookies=cookies, timeout=5)
    except:
        return "", 0, 0, 0
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract push messages
    pushes = soup.find_all("div", class_="push")
    push_count = 0
    boo_count = 0
    arrow_count = 0
    for p in pushes:
        tag = p.find("span", class_="push-tag")
        if tag:
            t = tag.text.strip()
            if '推' in t: push_count += 1
            elif '噓' in t: boo_count += 1
            else: arrow_count += 1
            
    # Extract main content
    main_content = soup.find("div", id="main-content")
    if not main_content:
        return "", push_count, boo_count, arrow_count
        
    # Remove meta info and push messages from main content to just get text
    for meta in main_content.find_all(['div', 'span']):
        meta.decompose()
        
    text = main_content.text
    # Clean text
    text = re.sub(r'※ 發信站: 批踢踢實業坊\(ptt.cc\).*', '', text, flags=re.DOTALL)
    text = re.sub(r'--\n.*', '', text, flags=re.DOTALL) # Remove signature
    text = re.sub(r'\n+', ' ', text)
    
    return text, push_count, boo_count, arrow_count

print("Starting scraping process...")
base_url = "https://www.ptt.cc/bbs/food/index.html"
all_articles = []

current_url = base_url
for i in range(10):
    print(f"Scraping page {i+1}...")
    articles, prev_url = get_page_articles(current_url)
    all_articles.extend(articles)
    if not prev_url:
        break
    current_url = prev_url
    time.sleep(0.5)

print(f"Total articles found: {len(all_articles)}")

data = []
all_words = []

for i, a in enumerate(all_articles):
    if i % 10 == 0:
        print(f"Processing article {i}/{len(all_articles)}")
    content, pc, bc, ac = get_article_content(a['url'])
    data.append({
        "Title": a['title'],
        "Type": a['type'],
        "Push": pc,
        "Boo": bc,
        "Net_Sentiment": pc - bc,
        "Content": content
    })
    
    # Jieba cut
    words = jieba.cut(content)
    for w in words:
        if len(w) > 1 and w not in STOPWORDS and not re.match(r'[a-zA-Z0-9]', w):
            all_words.append(w)
            
    time.sleep(0.1)

df = pd.DataFrame(data)

# 1. Type Analysis
print("\n--- Article Types Analysis ---")
type_counts = df['Type'].value_counts()
print(type_counts)

# Group by Type and get avg sentiment
type_sentiment = df.groupby('Type')['Net_Sentiment'].mean().sort_values(ascending=False)

# Plot Type Counts & Sentiment
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

type_counts.head(10).plot(kind='bar', ax=ax1, color='skyblue')
ax1.set_title('Top 10 文章類型數量')
ax1.set_ylabel('文章數')
ax1.tick_params(axis='x', rotation=45)

type_sentiment[type_counts.index[:10]].plot(kind='bar', ax=ax2, color='lightgreen')
ax2.set_title('Top 10 文章類型平均情緒分數 (推-噓)')
ax2.set_ylabel('平均情緒分數')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('type_analysis.png')
print("Saved type_analysis.png")

# 2. WordCloud
print("\n--- Generating WordCloud ---")
word_counts = Counter(all_words)
font_path = "C:/Windows/Fonts/msjh.ttc"
if not os.path.exists(font_path):
    font_path = None # Will try default if msjh not found

wc = WordCloud(
    font_path=font_path,
    background_color="white",
    width=800,
    height=400,
    max_words=100
)
wc.generate_from_frequencies(word_counts)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("PTT Food Top 10 Pages Word Cloud")
plt.tight_layout()
plt.savefig('wordcloud.png')
print("Saved wordcloud.png")

print("Analysis complete.")
df.to_csv('ptt_food_data.csv', index=False, encoding='utf-8-sig')
print("Saved data to ptt_food_data.csv")
