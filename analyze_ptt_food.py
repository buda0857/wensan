import os
import re
from collections import Counter

def analyze_ptt_food():
    dir_path = '.firecrawl'
    files = [f for f in os.listdir(dir_path) if f.startswith('ptt.cc-bbs-Food-') and f.endswith('.md')]
    
    titles = []
    categories = []
    regions = []
    
    for file in files:
        with open(os.path.join(dir_path, file), 'r', encoding='utf-8') as f:
            content = f.read()
            # PTT titles are usually in markdown links like: [[食記] 台北...]
            matches = re.findall(r'\[\\\[(.*?)\\\] (.*?)\]', content)
            # Sometimes firecrawl escapes brackets differently or they are just [[食記] ...]
            if not matches:
                matches = re.findall(r'\[\[(.*?)\] (.*?)\]', content)
            
            for cat, title in matches:
                categories.append(cat)
                titles.append(title)
                
                # Extract region (usually the first word in the title)
                region_match = re.search(r'^(\S+)', title)
                if region_match:
                    regions.append(region_match.group(1))

    # Perform analysis
    cat_counts = Counter(categories)
    region_counts = Counter(regions)
    
    # Common words in titles (excluding regions and stop words)
    words = []
    for title in titles:
        # Simple split by space/punctuation
        title_words = re.findall(r'[\u4e00-\u9fa5]{2,}', title)
        words.extend(title_words)
    
    word_counts = Counter(words)

    import json
    results = {
        "total_articles": len(titles),
        "categories": dict(cat_counts.most_common(10)),
        "regions": dict(region_counts.most_common(10)),
        "keywords": dict(word_counts.most_common(20))
    }
    
    with open('analysis_results.json', 'w', encoding='utf-8') as jf:
        json.dump(results, jf, ensure_ascii=False, indent=4)
    print("Analysis complete. Results saved to analysis_results.json")

if __name__ == "__main__":
    analyze_ptt_food()
