import random

mbti_data = {
    "INTJ": {"trait": "策略家，獨立、有遠見，擅長規劃未來。", "match": "ENFP, ENTP", "career": "科學家、工程師、軟體開發者", "dark_side": "控制欲強，情感壓抑，與人疏離。", "quote": "世界是為準備好的人設計的，而你正在設計它。"},
    "INTP": {"trait": "邏輯思維者，重視理論與分析，獨立思考。", "match": "ENTJ, ENFP", "career": "數據分析師、研究人員、哲學家", "dark_side": "逃避責任，遲疑不決，情緒冷淡。", "quote": "提問是通往真理的鑰匙。"},
    "ENTJ": {"trait": "天生領導者，果斷有野心，擅長規劃和指揮。", "match": "INFP, INTP", "career": "企業主管、律師、戰略顧問", "dark_side": "控制欲強、過度自信、不顧他人感受。", "quote": "你不只是夢想者，你是實現夢想的人。"},
    "ENTP": {"trait": "辯論家型，創新、有說服力，喜歡冒險與變化。", "match": "INFJ, INTJ", "career": "創意總監、發明家、創業者", "dark_side": "衝動、反覆無常、容易分心。", "quote": "點子不嫌多，重點是敢開始。"},
    "INFJ": {"trait": "理想主義者，洞察力強，致力於改變世界。", "match": "ENFP, ENTP", "career": "心理師、作家、教育者", "dark_side": "過度理想化、封閉自我、壓抑情感。", "quote": "即使孤獨，也要溫柔地照亮世界。"},
    "INFP": {"trait": "夢想家，忠於自我，充滿創造力與同理心。", "match": "ENFJ, ENTJ", "career": "藝術家、詩人、輔導員", "dark_side": "逃避現實、情緒低落、過度理想化。", "quote": "你心中的信念，就是你最大的力量。"},
    "ENFJ": {"trait": "領導型導師，善於激勵他人，溫暖有魅力。", "match": "INFP, ISFP", "career": "老師、人資、公關人員", "dark_side": "過度付出、自我犧牲、控制慾強。", "quote": "點燃別人靈魂的光，來自你心中的火。"},
    "ENFP": {"trait": "熱情奔放，富創意，渴望連結與自由。", "match": "INFJ, INTJ", "career": "記者、創意策劃、行銷人員", "dark_side": "情緒化、不專心、過度理想主義。", "quote": "你的熱情，是照亮世界的光源。"},
    "ISTJ": {"trait": "負責守紀律者，嚴謹實際，重視秩序與傳統。", "match": "ESFP, ESTP", "career": "會計、軍警、公務員", "dark_side": "固執、缺乏彈性、壓抑情緒。", "quote": "細節成就穩定，而穩定是你最強的優勢。"},
    "ISFJ": {"trait": "溫和的守護者，重視和諧與忠誠，樂於助人。", "match": "ESFP, ESTP", "career": "護理師、社工、行政人員", "dark_side": "壓抑自我、過度取悅、缺乏界限。", "quote": "溫柔的你，是最堅強的守護者。"},
    "ESTJ": {"trait": "管理型，組織能力強，重視效率與結果。", "match": "INFP, ISFP", "career": "經理人、警官、律師", "dark_side": "強勢、獨斷、情緒表達困難。", "quote": "帶領他人，是你的天賦。"},
    "ESFJ": {"trait": "社交高手，注重關係、善於合作與照顧他人。", "match": "ISTP, ISFP", "career": "教師、護士、客服代表", "dark_side": "過度關心他人、情緒依賴、害怕衝突。", "quote": "你讓世界變得更溫暖。"},
    "ISTP": {"trait": "實作高手，冷靜分析，擅長處理危機。", "match": "ESFJ, ENFJ", "career": "工程師、技術員、飛行員", "dark_side": "逃避責任、情感疏離、冷漠。", "quote": "用行動解決問題，是你與生俱來的能力。"},
    "ISFP": {"trait": "藝術靈魂，追求美與和諧，重視自由與體驗。", "match": "ENFJ, ESFJ", "career": "設計師、藝術家、攝影師", "dark_side": "逃避衝突、情緒化、不善溝通。", "quote": "你看見美，也創造美。"},
    "ESTP": {"trait": "冒險家，喜歡刺激與即興行動，實際又果斷。", "match": "ISFJ, ISTJ", "career": "業務、企業家、警察", "dark_side": "衝動、缺乏計畫、容易厭倦。", "quote": "把握當下，是你的超能力。"},
    "ESFP": {"trait": "活力四射，享受當下，帶動氣氛的快樂果。", "match": "ISFJ, ISTJ", "career": "演員、主持人、旅遊導遊", "dark_side": "缺乏耐心、害怕無聊、情緒反覆。", "quote": "你存在的地方，氣氛就亮起來了！"}
}

compatibility_map = {k: v["match"].split(", ") for k, v in mbti_data.items()}
tarot_cards = [
    "力量牌：你將克服內心的恐懼與挑戰。",
    "戀人牌：愛與選擇將成為未來的課題。",
    "倒吊人牌：等待與反思會帶來新的突破。",
    "命運之輪：命運的轉折正在逼近。",
    "太陽牌：你將迎來幸福與成就。",
    "塔牌：突如其來的改變將帶來成長。",
    "隱者牌：獨處與沉澱是前進的必經路。"
]

mbti_colors = {
    "INTJ": ("深紫色", "神秘冷靜"), "INTP": ("靛藍色", "理性深邃"), "ENTJ": ("深紅色", "果斷領導"),
    "ENTP": ("亮橘色", "活力創新"), "INFJ": ("灰紫色", "安靜洞察"), "INFP": ("淡藍綠", "夢幻柔和"),
    "ENFJ": ("暖粉色", "溫暖明亮"), "ENFP": ("珊瑚橘", "熱情多變"), "ISTJ": ("藏青色", "穩重守序"),
    "ISFJ": ("淺粉紫", "溫柔細膩"), "ESTJ": ("酒紅色", "自信強勢"), "ESFJ": ("玫瑰粉", "關懷親切"),
    "ISTP": ("金屬灰", "冷靜機敏"), "ISFP": ("森林綠", "自由靈感"), "ESTP": ("亮藍色", "行動直接"),
    "ESFP": ("亮黃色", "閃耀快樂")
}

social_tips = {
    "I": "主動傳訊問候朋友一下 😊", "E": "觀察他人情緒、少搶話 💬",
    "S": "留意熟人的細節並稱讚 👀", "N": "分享最近的創意想法 🌟",
    "T": "試著多問「你的感受是？」 🤝", "F": "今天勇敢表達情緒 💖",
    "J": "容許變動，放下控制 📅", "P": "完成一件拖延的小事 ✔️"
}

mbti_anime = {
    "INTJ": "夜神月（《死亡筆記本》）", "INTP": "石神千空（《Dr. STONE》）",
    "ENTJ": "利威爾（《進擊的巨人》）", "ENTP": "鬼塚英吉（《麻辣教師GTO》）",
    "INFJ": "伊魯卡老師（《火影忍者》）", "INFP": "愛蜜莉雅（《Re:從零》）",
    "ENFJ": "鳴人（《火影忍者》）", "ENFP": "路飛（《海賊王》）",
    "ISTJ": "一護爸爸（《BLEACH》）", "ISFJ": "小櫻（《火影忍者》）",
    "ESTJ": "張飛（《三國志》）", "ESFJ": "松田（《死亡筆記本》）",
    "ISTP": "坂田銀時（《銀魂》）", "ISFP": "千反田愛瑠（《冰菓》）",
    "ESTP": "佐助（《火影忍者》）", "ESFP": "小玉（《銀魂》）"
}

print("🎮 歡迎來到《MBTI密碼：揭開你靈魂的真相！》")
user_mbti = input("請輸入你的 MBTI 類型（如 INFP）：").upper()

if user_mbti not in mbti_data:
    print("❗ 錯誤：請輸入正確的 MBTI 類型。")
    exit()

data = mbti_data[user_mbti]
print("\n🧠 MBTI 性格分析：")
print("特徵：", data["trait"])
print("適合的朋友：", data["match"])
print("理想職涯：", data["career"])

if input("\n🎴 想抽一張命運塔羅牌嗎？(y/n): ").lower() == "y":
    print("🃏 你抽到的是：", random.choice(tarot_cards))

print("\n💑 試試看人格配對：")
other = input("請輸入你朋友/戀人的 MBTI：").upper()
if other in mbti_data:
    if other in compatibility_map[user_mbti]:
        print("💖 你們是高度契合的組合！")
    else:
        print("🤝 你們可能互補，需要溝通。")
else:
    print("⚠️ 無法辨識該 MBTI，略過配對。")

if input("\n🌒 想看你的暗人格嗎？(y/n): ").lower() == "y":
    print("🧠 暗人格揭示：", data["dark_side"])

print("\n💬 給你的 MBTI 勵志語錄：")
print("✨", data["quote"])


color, style = mbti_colors[user_mbti]
print("\n🎨 MBTI 配色建議：")
print(f"代表色：{color}，風格關鍵詞：{style}")

print("\n🎭 今日社交小建議：")
for c in user_mbti:
    if c in social_tips:
        print("👉", social_tips[c])

print("\n🔮 和你相像的動漫角色是：")
print("🌟", mbti_anime[user_mbti])

print("\n🎁 感謝遊玩《MBTI密碼》，祝你天天都有靈魂覺醒的一天！")
