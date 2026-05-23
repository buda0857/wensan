// ==========================================================================
// Obsidian Glassmorphism Blog Frontend Core Logic (Vanilla JS)
// ==========================================================================

// --- Embedded Dcard NLP Structured Analysis Dataset ---
const dcardData = {
  "overall": {
    "total_posts": 55,
    "total_likes": 3408,
    "total_comments": 2681,
    "sentiment_distribution": {
      "Positive": 21,
      "Neutral": 22,
      "Negative": 12
    }
  },
  "top_keywords": [
    {"text": "可以", "value": 11},
    {"text": "台灣", "value": 10},
    {"text": "官方", "value": 10},
    {"text": "討論", "value": 9},
    {"text": "有人", "value": 8},
    {"text": "他們", "value": 8},
    {"text": "這樣", "value": 7},
    {"text": "最近", "value": 7},
    {"text": "政治", "value": 6},
    {"text": "時事", "value": 6},
    {"text": "時間", "value": 6},
    {"text": "文化", "value": 5},
    {"text": "分享", "value": 5},
    {"text": "直接", "value": 5},
    {"text": "野外", "value": 5},
    {"text": "情感", "value": 5},
    {"text": "這種", "value": 5},
    {"text": "一下", "value": 5},
    {"text": "超商", "value": 5},
    {"text": "一定", "value": 4},
    {"text": "不好", "value": 4},
    {"text": "醫學", "value": 4},
    {"text": "房貸", "value": 4},
    {"text": "完全", "value": 4},
    {"text": "小孩", "value": 4},
    {"text": "機車", "value": 4},
    {"text": "問題", "value": 4},
    {"text": "認真", "value": 4},
    {"text": "朋友", "value": 4},
    {"text": "本來", "value": 4}
  ],
  "posts": [
    {
      "id": 1,
      "title": "喊出✨大學必做的事✨拿 5000 元夢想基金再讓 Dcard Video 陪你圓夢❤️‍🔥 #夢想派送計畫",
      "snippet": "大學是個很奇妙的地方🏫，長到可以修完 128 學分、熬夜 87 次、愛上 2 個人、後悔無數件事💔，卻又短到一轉眼就結束了💫，上大學前許願想完成的事，你都做了嗎？有些事，再不做就真的沒機會了🫵...",
      "link": "https://www.dcard.tw/f/talk",
      "likes": 765,
      "comments": 359,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 2,
      "title": "#集中討論 文化幣邀請碼分享",
      "snippet": "近日因文化幣發送，我們發現站上有許多人會分享邀請碼以賺取更多文化幣，小天使特地開此討論串，讓大家能夠盡情分享邀請碼！在發送你的邀請碼前，請務必注意相關全站規範...",
      "link": "https://www.dcard.tw/f/talk",
      "likes": 380,
      "comments": 550,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 3,
      "title": "#公告 時事、政治相關議題請至時事板發表",
      "snippet": "各位卡友們好，我們始終努力維持一個友善的討論環境，並鼓勵大家到各個看板討論符合板旨的議題；由於近期有許多政治類型的討論文章發表在閒聊板中，請各位卡友留意...",
      "link": "https://www.dcard.tw/f/talk",
      "likes": 309,
      "comments": 580,
      "sentiment": "Positive",
      "sentiment_score": 0.7
    },
    {
      "id": 4,
      "title": "嘴擎天崗五分鐘一定沒玩過",
      "snippet": "野砲五分鐘其實不短了，在外面享受的是刺激的爽感，隨時都有可能被發現，誰跟你慢慢做啊🤣，當然是速戰速決，我自己跟另一半也是很常在野外，時間基本都不超過五分鐘，但在床上根本不可能那麼短，野外也不好換姿勢...",
      "link": "https://www.dcard.tw/f/talk/p/261522605",
      "likes": 298,
      "comments": 100,
      "sentiment": "Positive",
      "sentiment_score": 0.7
    },
    {
      "id": 5,
      "title": "NONO 要入獄了",
      "snippet": "NONO 因涉性侵猥褻 6 女其中一案成立，依強制性交未遂判 2 年 6 個月，昨天上訴期限正式屆滿，台灣高等檢察署決定不再提上訴，說二審判決沒有違背法令，希望判決早日確定、讓他入監服刑...",
      "link": "https://www.dcard.tw/f/talk/p/261523599",
      "likes": 360,
      "comments": 91,
      "sentiment": "Negative",
      "sentiment_score": 0.2
    },
    {
      "id": 6,
      "title": "擎天崗野戰情侶到案了",
      "snippet": "上週擎天崗直播野戰的事，這兩天終於有後續了，兩人在 17 日低調前往警局製作筆錄，也坦承自己就是影片中的男女主角，據說一開始男方說要請假去，後來又沒出現，最後才終於去了，兩人都說不知道現場有攝影機...",
      "link": "https://www.dcard.tw/f/talk/p/261524325",
      "likes": 289,
      "comments": 51,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 7,
      "title": "台男霸凌女同學：吃我的屌",
      "snippet": "台北市一名國中三年級女學生，長期遭受同班男同學言語霸凌及性騷擾，17日會考中午時，男同學竟在考場開黃腔，甚至嗆「吃我的Ｘ」，女學生憤而揍對方肚子一拳，未料男同學隨即反擊，不僅將她踢倒在地，更出拳毆打臉部至少三拳...",
      "link": "https://www.dcard.tw/f/talk/p/261522678",
      "likes": 175,
      "comments": 69,
      "sentiment": "Negative",
      "sentiment_score": 0.2
    },
    {
      "id": 8,
      "title": "不小心看到送肉粽怎麼辦",
      "snippet": "如題，近期實在太多相關文章了，剛剛無聊滑脆，結果有網友去朝聖 甚至把畫面拍下來，然後我看到了好像，不過只看到喵到道士，我應該做些什麼嗎。。。網路上看到也算嗎，我保持敬畏的心但還是怕怕的不知道怎麼辦..",
      "link": "https://www.dcard.tw/f/talk/p/261519798",
      "likes": 71,
      "comments": 141,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 9,
      "title": "2027 年的連假出來了",
      "snippet": "全年總放假日 121 天！！！，而且有 9 個 3 天以上的連假，春節連休 7 天，今年還沒過一半，已經開始期待明年了，不說了我要先來安排出國（？",
      "link": "https://www.dcard.tw/f/talk/p/261524534",
      "likes": 87,
      "comments": 15,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 10,
      "title": "一回到家，直接砲轟警局",
      "snippet": "是這樣的，回到家我發現我的東西全部被環保局清運掉，是的，我被檢舉，但我只是把東西堆家門口，因為，租屋處空間很小，實在堆不了太多東西。看到被舉發，我很傻眼，是怎樣？我是把東西放路中間還是擋消防通道？",
      "link": "https://www.dcard.tw/f/talk/p/261520344",
      "likes": 48,
      "comments": 88,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 11,
      "title": "北市中山死亡車禍！無照男持影本租車撞死騎士　還是違規大戶積欠40張罰單",
      "snippet": "北市中山區吉林路與長春路口19日上午8時許發生一起死亡車禍事故。一名黃姓男子駕駛租賃車輛行經該處時，與一名許姓騎士發生擦撞，強大撞擊力道當場造成許姓騎士被撞飛，緊急送醫後仍不幸不治...",
      "link": "https://www.dcard.tw/f/talk/p/261522258",
      "likes": 82,
      "comments": 47,
      "sentiment": "Negative",
      "sentiment_score": 0.0
    },
    {
      "id": 12,
      "title": "台大台男：憑實力把男宿住成女宿",
      "snippet": "台大男宿的台男有福了，憑藉實力直接把男宿打造住成女宿的風格在網路上引起熱議...",
      "link": "https://www.dcard.tw/f/talk/p/261525226",
      "likes": 61,
      "comments": 17,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 13,
      "title": "被鬼壓床原本要去拜拜，後來才發現是我有病",
      "snippet": "各位…，我前幾天真的以為自己要被帶走😢，現在還餘悸猶存，那天只是加班加比較晚，回家洗好澡就直接躺平，結果半夜突然半夢半醒，感覺醒了 但整個人又完全動不了，還一直聽到有人在叫我，胸口超悶 像被壓住...",
      "link": "https://www.dcard.tw/f/talk/p/261523709",
      "likes": 43,
      "comments": 11,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 14,
      "title": "每個月5千還是不想生",
      "snippet": "補，只有我覺得大家厭童，絕大部分是被狼性職場搞出來的嗎，以前我都覺得有小孩的人，一定是家裡後院有石油的那種人，所以在路上看到親子，總覺得這是某種炫耀行為...",
      "link": "https://www.dcard.tw/f/talk/p/261520789",
      "likes": 30,
      "comments": 86,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 15,
      "title": "大家知道什麼是生物膜嗎？",
      "snippet": "上禮拜跟同學一起去宜蘭包棟過夜，才發現居然有人不知道生物膜是什麼😳，我以為這是生活常識耶！！，簡單講生物膜就是細菌聚集後形成的一層黏黏滑滑的膜，超常出現在水槽排水口、浴室磁磚縫...",
      "link": "https://www.dcard.tw/f/talk/p/261522379",
      "likes": 46,
      "comments": 22,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 16,
      "title": "大家最近也開始感受到畢業即失業了嗎…",
      "snippet": "今年應屆畢業的大家都開始找工作了嗎？這陣子投了好多家職缺，每一次按出送出履歷，心裡都抱著一絲期待，結果換來的只有無止境的已讀不回。 看著那些投遞狀態從未讀變成已讀，然後就再也沒有然後了...",
      "link": "https://www.dcard.tw/f/talk/p/261524084",
      "likes": 22,
      "comments": 24,
      "sentiment": "Negative",
      "sentiment_score": 0.3
    },
    {
      "id": 17,
      "title": "台男：醫學系的課是我聽到最多歧視性別跟種族的地方",
      "snippet": "台男認證的醫學系台男最愛歧視性別跟種族，文章發出後引發醫學生與其他卡友之間的熱烈論戰...",
      "link": "https://www.dcard.tw/f/talk/p/261525964",
      "likes": 20,
      "comments": 33,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 18,
      "title": "家人過世請益",
      "snippet": "我的父親在前幾天過世了，名下有許多東西（車子、機車、房子、財產）等等。目前尚未辦除戶，財產為母親與我平分繼承，請問除戶之前可以將郵局及銀行的錢領出嗎？目前汽機車過戶要怎麼辦理？",
      "link": "https://www.dcard.tw/f/talk/p/261524950",
      "likes": 9,
      "comments": 13,
      "sentiment": "Negative",
      "sentiment_score": 0.4
    },
    {
      "id": 19,
      "title": "不主動、不拒絕、不負責",
      "snippet": "女人真的別以為，男人對妳有點主動、有點曖昧，妳就能拿捏他的心態。很多時候，妳以為自己在拉扯他，其實人家心裡根本超清楚。他知道妳在釋放好感，但又故意不讓他真的得到，不就是想看他會不會先付出...",
      "link": "https://www.dcard.tw/f/talk/p/261521331",
      "likes": 20,
      "comments": 11,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 20,
      "title": "外國人：感受到台灣人心險惡，但我能忍受",
      "snippet": "台灣人現在對外國人愈來愈不友善了，來台長住的外籍網友發文抒發對台灣日常生活與職場文化中人情冷暖的深刻感受...",
      "link": "https://www.dcard.tw/f/talk/p/261519312",
      "likes": 12,
      "comments": 3,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 21,
      "title": "外國人：台鐵應該設立茹素專用車廂",
      "snippet": "台灣實在太落後了，除了女性專屬車廂，應該還要有茹素專屬車廂，台灣不加緊腳步跟上國際，難怪國旅發展失敗，連外國人都看不下去，此言一出引發吃素與吃肉卡友論戰...",
      "link": "https://www.dcard.tw/f/talk/p/261516000",
      "likes": 15,
      "comments": 40,
      "sentiment": "Negative",
      "sentiment_score": 0.3
    },
    {
      "id": 22,
      "title": "現在超商整齊標準都要這麼高嗎",
      "snippet": "如題，看到threads上有人發了這個，我嘖嘖稱奇，確實看起來很賞心悅目沒錯，但我真的是很好奇店員要排成這樣要花多少時間啊，要不就是他有強迫症或是完美主義心態，要不就是生意不好所以他有大把時間...",
      "link": "https://www.dcard.tw/f/talk/p/261519525",
      "likes": 25,
      "comments": 4,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 23,
      "title": "iwin的兒童及少年福利與權益保障法修正草案看起來超級危險",
      "snippet": "連結內是前版上的討論，大致整理了修改後的問題：一、 擴大權能夠硬性封網，相較於原本沒有的定義，修法後幾乎將整個台灣的網路生態全面納入管轄...",
      "link": "https://www.dcard.tw/f/talk/p/261522470",
      "likes": 18,
      "comments": 6,
      "sentiment": "Negative",
      "sentiment_score": 0.4
    },
    {
      "id": 24,
      "title": "衛福部又想搞鬼了",
      "snippet": "他們弄了一個這個，其中 第59條寫了，說人話 他可以不跑任何流程直接封網，然後最嚴重的，是年齡識別標準的制定與技術要求，恐侵害網路言論自由與隱私權...",
      "link": "https://www.dcard.tw/f/talk/p/261347486",
      "likes": 16,
      "comments": 9,
      "sentiment": "Neutral",
      "sentiment_score": 0.5
    },
    {
      "id": 25,
      "title": "油煙機換新求建議！",
      "snippet": "舊的抽油煙機因為卡油刷不掉，感覺吸力變得很無感，想換進風口離鍋子近的款式，目前在看櫻花的DR7397，不知道這種近吸式攔截油煙的效果好嗎？另外想問它的靜音除味功能，運轉聲音會不會很大？",
      "link": "https://www.dcard.tw/f/talk/p/261522282",
      "likes": 15,
      "comments": 6,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 26,
      "title": "簡直跟猴子一樣",
      "snippet": "在蔦屋書店跟星巴克附設的座位吃 「韭菜」煎包， 還有看手機音量開大聲， 真的是跟猴子一樣，有夠扯，猩球崛起裡的都比這隻有文化...",
      "link": "https://www.dcard.tw/f/talk/p/261522712",
      "likes": 9,
      "comments": 7,
      "sentiment": "Negative",
      "sentiment_score": 0.4
    },
    {
      "id": 27,
      "title": "有人會把打手槍後的衛生紙暫時放在電腦機殼嗎",
      "snippet": "剛打完手槍的衛生紙都會有很明顯的味道，如果馬上丟垃圾桶其他人打開一下很快就聞到了，放在在房間也有味道，後來發現可以放電腦機殼裡而且很通風不會有異味，隔天拿出來就乾了很方便...",
      "link": "https://www.dcard.tw/f/talk/p/261525575",
      "likes": 11,
      "comments": 17,
      "sentiment": "Negative",
      "sentiment_score": 0.4
    },
    {
      "id": 28,
      "title": "啊勞越來越多",
      "snippet": "今天在自習室遇到啊勞 香水味整間都是就算了 手機不關靜音通知狂跳 脫拖鞋盤腿坐 在看他了繼續大聊特聊 好奇在他們國家在圖書館這樣很正常嗎？如果遇到這種又語言不通要怎麼處理？除了抓去當工人...",
      "link": "https://www.dcard.tw/f/talk/p/261525492",
      "likes": 6,
      "comments": 2,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 29,
      "title": "如果你的命必須殺人續命你會去做嗎？",
      "snippet": "看完〈國有器官〉 我跟男友大吵一架…… 我一直以為大部分人都跟我一樣，即使到了窮途末路的時候，也絕對不會為了自己活命而害人，畢竟從小到大都被教要當個好人，但男友卻說，如果為了親人活命他一定會...",
      "link": "https://www.dcard.tw/f/talk/p/261526170",
      "likes": 7,
      "comments": 15,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    },
    {
      "id": 30,
      "title": "[閒聊] 被寶雅店員朋友推坑的瞬暢果凍，認真有效💩",
      "snippet": "上次跟一個在寶雅上班的朋友吃飯，聊到我最近因為壓力大，肚子脹到快炸開，每次去廁所都會蹲到腳麻，本來真的打算去藥局買那種強效便秘藥了，結果我朋友叫我冷靜，說那種藥不能亂吃，吃久了腸胃會變得很懶惰...",
      "link": "https://www.dcard.tw/f/talk/p/261522237",
      "likes": 8,
      "comments": 5,
      "sentiment": "Positive",
      "sentiment_score": 0.6
    }
  ]
};

// --- Page Initialization Hub ---
document.addEventListener("DOMContentLoaded", () => {
    // Determine which page we are on
    if (document.getElementById("dcard-posts-grid")) {
        initAnalyticsPage();
    } else if (document.getElementById("recent-posts-list")) {
        initHomePage();
    }
});

// --- Home Page Setup ---
function initHomePage() {
    const listContainer = document.getElementById("recent-posts-list");
    if (!listContainer) return;

    // Render Dcard Analysis project as the featured top article in list
    const dcardPostHTML = `
        <article class="post-card glass-card">
            <div class="post-meta">
                <span class="tag">數據分析</span>
                <span>2026 年 5 月 23 日</span>
                <span>💬 141 則討論</span>
            </div>
            <h3><a href="dcard-analysis.html">Dcard 閒聊板熱門數據庫：情感極性與斷詞文字雲大揭密！</a></h3>
            <p>利用現代 AI 數據抓取引擎 Firecrawl 與中文自然語言處理（NLP）技術，深入剖析 Dcard 閒聊板（Talk）最新前 30 則熱門貼文，探索年輕世代的核心關鍵字與當前網路輿論的情感流向...</p>
            <div>
                <a href="dcard-analysis.html" class="read-more">進入分析看板 →</a>
            </div>
        </article>
    `;
    
    listContainer.insertAdjacentHTML("afterbegin", dcardPostHTML);
}

// --- Analytics Dashboard Setup ---
function initAnalyticsPage() {
    // 1. Dynamic Statistic Counter Animation
    animateCounter("stat-total-posts", dcardData.overall.total_posts, 1500);
    animateCounter("stat-total-likes", dcardData.overall.total_likes, 1500);
    animateCounter("stat-total-comments", dcardData.overall.total_comments, 1500);

    // 2. Render SVG Donut Chart
    renderSentimentDonut();

    // 3. Render Keywords Badges List
    renderKeywordBadges();

    // 4. Render and Bind Post Grid Filter
    renderPostsGrid(dcardData.posts);
    bindFilters();
}

// --- Dynamic Counter Helper ---
function animateCounter(id, targetValue, duration) {
    const el = document.getElementById(id);
    if (!el) return;
    
    let start = 0;
    const stepTime = Math.abs(Math.floor(duration / targetValue));
    
    // Avoid too slow loops on large numbers
    const increment = Math.max(1, Math.floor(targetValue / 60));
    
    const timer = setInterval(() => {
        start += increment;
        if (start >= targetValue) {
            el.textContent = targetValue.toLocaleString();
            clearInterval(timer);
        } else {
            el.textContent = start.toLocaleString();
        }
    }, Math.min(20, stepTime));
}

// --- Render SVG Donut Chart ---
function renderSentimentDonut() {
    const container = document.getElementById("sentiment-donut-container");
    if (!container) return;

    const positive = dcardData.overall.sentiment_distribution.Positive;
    const neutral = dcardData.overall.sentiment_distribution.Neutral;
    const negative = dcardData.overall.sentiment_distribution.Negative;
    const total = positive + neutral + negative;

    // Percentages
    const pctPos = (positive / total) * 100;
    const pctNeu = (neutral / total) * 100;
    const pctNeg = (negative / total) * 100;

    // Circle properties: r=50, C = 2 * pi * r = 314.159
    const circumference = 314.159;
    
    // Stroke Dasharrays
    const dashPos = `${(pctPos / 100) * circumference} ${circumference}`;
    const dashNeu = `${(pctNeu / 100) * circumference} ${circumference}`;
    const dashNeg = `${(pctNeg / 100) * circumference} ${circumference}`;

    // Cumulative stroke offsets
    const offsetPos = 0;
    const offsetNeu = -((pctPos / 100) * circumference);
    const offsetNeg = -(((pctPos + pctNeu) / 100) * circumference);

    const svgHTML = `
        <svg width="220" height="220" viewBox="0 0 120 120" style="filter: drop-shadow(0 8px 16px rgba(0,0,0,0.5));">
            <!-- Background base circle -->
            <circle cx="60" cy="60" r="50" fill="transparent" stroke="rgba(255,255,255,0.03)" stroke-width="8" />
            
            <!-- Positive Segment -->
            <circle class="donut-segment" cx="60" cy="60" r="50" 
                    fill="transparent" stroke="var(--color-positive)" stroke-width="10" 
                    stroke-dasharray="${dashPos}" stroke-dashoffset="${offsetPos}"
                    data-sentiment="Positive" data-value="${positive}" />
                    
            <!-- Neutral Segment -->
            <circle class="donut-segment" cx="60" cy="60" r="50" 
                    fill="transparent" stroke="var(--color-neutral)" stroke-width="10" 
                    stroke-dasharray="${dashNeu}" stroke-dashoffset="${offsetNeu}"
                    data-sentiment="Neutral" data-value="${neutral}" />
                    
            <!-- Negative Segment -->
            <circle class="donut-segment" cx="60" cy="60" r="50" 
                    fill="transparent" stroke="var(--color-negative)" stroke-width="10" 
                    stroke-dasharray="${dashNeg}" stroke-dashoffset="${offsetNeg}"
                    data-sentiment="Negative" data-value="${negative}" />

            <!-- Donut Center Label -->
            <g class="donut-label-group" transform="translate(60, 60)" style="text-anchor: middle;">
                <text y="-2" class="donut-label" id="donut-center-title">${Math.round(pctPos + pctNeu)}%</text>
                <text y="14" class="donut-sub" id="donut-center-sub">非負面情緒比例</text>
            </g>
        </svg>
    `;

    container.innerHTML = svgHTML;

    // Interactive segment hover listeners
    const segments = container.querySelectorAll(".donut-segment");
    const centerTitle = document.getElementById("donut-center-title");
    const centerSub = document.getElementById("donut-center-sub");

    segments.forEach(seg => {
        seg.addEventListener("mouseenter", () => {
            const sentiment = seg.getAttribute("data-sentiment");
            const val = seg.getAttribute("data-value");
            const percentage = Math.round((val / total) * 100);
            
            let labelText = "正向情緒";
            if (sentiment === "Neutral") labelText = "中立情緒";
            if (sentiment === "Negative") labelText = "負向情緒";
            
            centerTitle.textContent = `${percentage}%`;
            centerTitle.style.fill = `var(--color-${sentiment.toLowerCase()})`;
            centerSub.textContent = `${labelText} (${val} 篇)`;
        });

        seg.addEventListener("mouseleave", () => {
            const nonNegPct = Math.round(((positive + neutral) / total) * 100);
            centerTitle.textContent = `${nonNegPct}%`;
            centerTitle.style.fill = `var(--color-text-primary)`;
            centerSub.textContent = "非負面情緒比例";
        });
    });
}

// --- Render Keywords Badges ---
function renderKeywordBadges() {
    const list = document.getElementById("keyword-badges-list");
    if (!list) return;

    list.innerHTML = dcardData.top_keywords.map((kw, i) => {
        // Calculate heat category based on index
        let heatClass = "heat-low";
        if (i < 5) heatClass = "heat-high";
        else if (i < 15) heatClass = "heat-med";
        
        return `<span class="keyword-badge ${heatClass}" title="提及頻率: ${kw.value} 次">${kw.text} <small>${kw.value}</small></span>`;
    }).join("");
}

// --- Render Dcard Posts Grid ---
function renderPostsGrid(posts) {
    const grid = document.getElementById("dcard-posts-grid");
    if (!grid) return;

    if (posts.length === 0) {
        grid.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 4rem; color: var(--color-text-muted);">
                <p style="font-size: 1.2rem; margin-bottom: 0.5rem;">無符合搜尋條件的討論資料</p>
                <small>請嘗試調整過濾標籤或搜尋關鍵字</small>
            </div>
        `;
        return;
    }

    grid.innerHTML = posts.map(p => {
        const sentimentClass = `sentiment-${p.sentiment.toLowerCase()}`;
        let sentimentText = "正向";
        if (p.sentiment === "Neutral") sentimentText = "中立";
        if (p.sentiment === "Negative") sentimentText = "負向";

        return `
            <div class="glass-card dcard-card" data-sentiment="${p.sentiment}">
                <div class="dcard-card-header">
                    <span class="sentiment-badge ${sentimentClass}">${sentimentText} (${p.sentiment_score})</span>
                    <span style="color: var(--color-text-muted); font-size: 0.8rem;">ID: #${p.id}</span>
                </div>
                <h4 style="margin-bottom: 0.75rem;">
                    <a href="${p.link}" target="_blank">${p.title}</a>
                </h4>
                <p class="dcard-desc">${p.snippet}</p>
                <div class="dcard-footer">
                    <div class="dcard-stats">
                        <span>👍 ${p.likes} 反應</span>
                        <span>💬 ${p.comments} 留言</span>
                    </div>
                    <a href="${p.link}" target="_blank" class="read-more" style="font-size: 0.85rem;">前往 Dcard 閱讀 →</a>
                </div>
            </div>
        `;
    }).join("");
}

// --- Bind Interactive Search and Filters ---
function bindFilters() {
    const searchInput = document.getElementById("search-input");
    const filterTags = document.querySelectorAll(".filter-tag");
    
    let currentSentiment = "All";
    let currentQuery = "";

    const performFilter = () => {
        let filtered = dcardData.posts;

        // Apply Sentiment Filter
        if (currentSentiment !== "All") {
            filtered = filtered.filter(p => p.sentiment === currentSentiment);
        }

        // Apply Search Term Filter
        if (currentQuery.trim() !== "") {
            const q = currentQuery.toLowerCase();
            filtered = filtered.filter(p => 
                p.title.toLowerCase().includes(q) || 
                p.snippet.toLowerCase().includes(q)
            );
        }

        renderPostsGrid(filtered);
    };

    // Bind Search Input
    if (searchInput) {
        searchInput.addEventListener("input", (e) => {
            currentQuery = e.target.value;
            performFilter();
        });
    }

    // Bind Filter Tabs
    filterTags.forEach(tag => {
        tag.addEventListener("click", () => {
            filterTags.forEach(t => t.classList.remove("active"));
            tag.classList.add("active");
            
            currentSentiment = tag.getAttribute("data-filter");
            performFilter();
        });
    });
}
