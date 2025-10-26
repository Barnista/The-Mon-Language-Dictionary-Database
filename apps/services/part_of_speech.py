pos_thai_eng = {
    "น.": "n", # noun
    "ส.": "pron", # pronoun 
    "ก.": "v", # verb
    "ว.": "adv", # adverb
    "บุพ.": "prep", # preposition
    "สัน.": "conj", # conjunction
    "อุ.": "interj", # interjection
    "ลน.": "clf", # classifier
    "ไว.": "art.", # article
    "อุปสรรค.": "prefix", # prefix
    "ปัจจัย.": "suffix", # suffix
    "สำนวน.": "idiom", # idiom
    "สุภาษิต.": "proverb" # proverb,
}

# Function to get English POS code from Thai POS tag
def get_pos_code_from_thai_tag(thai_tag):
    return pos_thai_eng.get(thai_tag, "other")