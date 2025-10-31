# Converted from JS to Python
class LibDoubleConsonant:
    def __init__(self):
        self.exampleDirect = [
            {
                "word": "လ္ပ",
                "full": "လပ",
                "ipa": "lɛ̤ˀpaˀ",
                "th": "เลี่ยะปะ",
                "translates": [
                    {"type": "ว.", "meaning": "อย่า"},
                    {"type": "ก.", "meaning": "อย่าทำ"},
                ],
            },
            {
                "word": "သ္ပ",
                "full": "သပ",
                "ipa": "saˀpaˀ",
                "th": "ซะปะ",
                "translates": [
                    {"type": "ก.", "meaning": "กระทำ"},
                    {"type": "ก.", "meaning": "จะทำ"},
                ],
            },
            {
                "word": "က္တဵု",
                "full": "ကတဵု",
                "ipa": "kaˀtɒw",
                "th": "กะตอว",
                "translates": [{"type": "น.", "meaning": "กะท้อน"}],
            },
            {
                "word": "လ္တူ",
                "full": "လတူ",
                "ipa": "lɛ̤ˀtao",
                "th": "เลี่ยะตาว",
                "translates": [
                    {"type": "บุพ.", "meaning": "บน"},
                    {"type": "บุพ.", "meaning": "เหนือ"},
                ],
            },
            {
                "word": "ခဗ္ဒာဲ",
                "full": "ခဗဒာယ်",
                "ipa": "kʰaˀpɛ̤ˀta̤i",
                "th": "ขะเปี่ยต่าย",
                "translates": [
                    {"type": "ก.", "meaning": "อาศัย"},
                    {"type": "ก.", "meaning": "พึ่งพิง"},
                ],
            },
        ]

        self.examplePaliSansakrit = [
            # ROW-1
            {"row": 1, "column": 1, "doubleWith": 1, "word": "သက္ကရာဇ်", "full": "သက်ကရာဇ်", "ipa": "saˀkkaˀra̤c", "th": "ซักกะราจ"},
            {"row": 1, "column": 1, "doubleWith": 2, "word": "စက္ခု", "full": "စက်ခု", "ipa": "caˀkkʰùˀ", "th": "จักขุ"},
            {"row": 1, "column": 3, "doubleWith": 3, "word": "အဂ္ဂ", "full": "အဂ်ဂ", "ipa": "ʔaˀkkɛ̤ˀ", "th": "อักเกี่ยะ"},
            {"row": 1, "column": 3, "doubleWith": 4, "word": "အနဂ္ဃ", "full": "အနဂ်ဃ", "ipa": "ʔaˀnɛˀkkʰɛ̤ˀ", "th": "อะแน่กเคี่ยะ"},
            {"row": 1, "column": 5, "doubleWith": 5, "word": "", "full": "", "ipa": "", "th": ""},
            {"row": 1, "column": 5, "doubleWith": 3, "word": "မၚ်္ဂလ", "full": "မင်ဂလ", "ipa": "mɛˀŋkɛ̤ˀlɛ̤ˀ", "th": "แม่งเกี่ยะเลี่ยะ"},
            # ROW-2
            {"row": 2, "column": 1, "doubleWith": 1, "word": "သစ္စ", "full": "သစ်စ", "ipa": "sɒccaˀ", "th": "ซอจจะ", "th2": "ซอจเจีย"},
            {"row": 2, "column": 1, "doubleWith": 2, "word": "မိစ္ဆာ", "full": "မိစ်ဆာ", "ipa": "mìˀccʰa", "th": "มิ่จฉา"},
            {"row": 2, "column": 3, "doubleWith": 3, "word": "အဇ္ဇေ", "full": "အဇ်ဇေ", "ipa": "ʔɒccè", "th": "ออจเจ่"},
            {"row": 2, "column": 3, "doubleWith": 4, "word": "ဥပ္ပဇ္ၛာဲ", "full": "ဥပ်ပဇ်ၛာဲ", "ipa": "ùˀppòccʰa̤i", "th": "อุปปอจช่าย", "th2": "อุปอจช่าย"},
            {"row": 2, "column": 5, "doubleWith": 5, "word": "ပညာ", "full": "ပည်ညာ", "ipa": "pɒɲɲɛ̀a", "th": "ปอญเญีย", "th2": "ปอญญา"},
            # ROW-3
            {"row": 3, "column": 1, "doubleWith": 1, "word": "ဝဋသံသာ", "full": "ဝဋ်ဋသံသာ", "ipa": "wòttaˀsɔmˀsa", "th": "โว่ดตะซอมซา"},
            {"row": 3, "column": 1, "doubleWith": 2, "word": "သတိသံပဋ္ဌာနံ", "full": "သတိသံပဋ်ဌာနံ", "ipa": "saˀtɔɪsɔmˀpɒttʰanòm", "th": "ซะต็อยซอมปอดทาน่ม", "th2": "ซะต็อยซอมปอดทาน่อง"},
            {"row": 3, "column": 3, "doubleWith": 3, "word": "", "full": "", "ipa": "", "th": ""},
            {"row": 3, "column": 3, "doubleWith": 4, "word": "ဝဍ္ဎန", "full": "ဝဋ်ဎန", "ipa": "wòttʰɛ̤ˀnɛ̤ˀ", "th": "โว่ดเที่ยะเนี่ยะ"},
            {"row": 3, "column": 5, "doubleWith": 5, "word": "ဝဏ္ဏ", "full": "ဝဏ်ဏ", "ipa": "wònnaˀ", "th": "โว่นนะ"},
            {"row": 3, "column": 5, "doubleWith": 2, "word": "သဏ္ဌာန", "full": "သဏ်ဌာန", "ipa": "sɒntʰanɛ̤ˀ", "th": "ซอนทาเนี่ยะ", "th2": "ซอนทานะ"},
            # ROW-4
            {"row": 4, "column": 1, "doubleWith": 1, "word": "ကတ္တိက", "full": "ကတ်တိက", "ipa": "kɒttɔɪkaˀ", "th": "กอดต็อยกะ"},
            {"row": 4, "column": 1, "doubleWith": 2, "word": "ဝတ္ထ", "full": "ဝတ်ထ", "ipa": "wòttʰaˀ", "th": "โว่ดทะ"},
            {"row": 4, "column": 3, "doubleWith": 3, "word": "သဒ္ဒါ", "full": "သဒ်ဒါ", "ipa": "sɒttɛ̀a", "th": "ซอดเตี่ย"},
            {"row": 4, "column": 5, "doubleWith": 4, "word": "ခန္ဓ", "full": "ခန်ဓ", "ipa": "kʰɒntʰɛ̤ˀ", "th": "คอนเที่ยะ"},
            # ROW-5
            {"row": 5, "column": 1, "doubleWith": 1, "word": "သိပ္ပံ", "full": "သိပ်ပံ", "ipa": "sɔeˀppɔmˀ", "th": "ซิบปอม", "th2": "ซิบปอง"},
            {"row": 5, "column": 1, "doubleWith": 2, "word": "ပုပ္ဖ", "full": "ပုပ်ဖ", "ipa": "pùˀpʰaˀ", "th": "ปุบพะ"},
            {"row": 5, "column": 3, "doubleWith": 3, "word": "သဗ္ဗ", "full": "သဗ်ဗ", "ipa": "sɒppɛ̤ˀ", "th": "ซอบเปี่ยะ"},
            {"row": 5, "column": 3, "doubleWith": 4, "word": "ဂဗ္ဘ", "full": "ဂဗ်ဘ", "ipa": "kòppʰɛ̤ˀ", "th": "โก่บเพี่ยะ"},
            {"row": 5, "column": 5, "doubleWith": 5, "word": "ဓမ္မ", "full": "ဓမ်မ", "ipa": "tʰòmmɛ̤ˀ", "th": "โท่มเมี่ยะ"},
            {"row": 5, "column": 5, "doubleWith": 3, "word": "သမ္ဗုဒ္ဓ", "full": "သမ်ဗုဒ်ဓ", "ipa": "sɒmpùˀttʰɛ̤ˀ", "th": "ซอมปุ่ดเที่ยะ"},
            # ROW-none
            {"row": 6, "column": 3, "doubleWith": 3, "word": "ပလ္လၚ်္က", "full": "ပလ်လင်က", "ipa": "pɒllɛˀŋkaˀ", "th": "ปอลแล่งกะ", "th2": "ปอนลังกะ"},
            {"row": 6, "column": 5, "doubleWith": 5, "word": "တသ္သ", "full": "တသ်သ", "ipa": "tɒssaˀ", "th": "ตอดซะ"},
        ]

        # กฎที่ระบุว่าพยัญชนะซ้อนแบบบาลี-สันสกฤต ตัวใดซ้อนกับตัวใดได้บ้าง
        self.paliSansakrits = [
            # ROW-1
            {"row": 1, "column": 1, "doubleWith": 1, "consonant": "က", "overlapped": "က", "letter": "က္က", "converts": ["က်", "က"]},
            {"row": 1, "column": 1, "doubleWith": 2, "consonant": "က", "overlapped": "ခ", "letter": "က္ခ", "converts": ["က်", "ခ"]},
            {"row": 1, "column": 3, "doubleWith": 3, "consonant": "ဂ", "overlapped": "ဂ", "letter": "ဂ္ဂ", "converts": ["ဂ်", "ဂ"]},
            {"row": 1, "column": 3, "doubleWith": 4, "consonant": "ဂ", "overlapped": "ဃ", "letter": "ဂ္ဃ", "converts": ["ဂ်", "ဃ"]},
            # letter ၚ is an exception (commented out in original)
            {"row": 1, "column": 5, "doubleWith": 1, "consonant": "ၚ", "overlapped": "က", "letter": "ၚ်္က", "converts": ["ၚ်", "က"]},
            {"row": 1, "column": 5, "doubleWith": 2, "consonant": "ၚ", "overlapped": "ခ", "letter": "ၚ်္ခ", "converts": ["ၚ်", "ခ"]},
            {"row": 1, "column": 5, "doubleWith": 3, "consonant": "ၚ", "overlapped": "ဂ", "letter": "ၚ်္ဂ", "converts": ["ၚ်", "ဂ"]},
            {"row": 1, "column": 5, "doubleWith": 4, "consonant": "ၚ", "overlapped": "ဃ", "letter": "ၚ်္ဃ", "converts": ["ၚ်", "ဃ"]},
            # ROW-2
            {"row": 2, "column": 1, "doubleWith": 1, "consonant": "စ", "overlapped": "စ", "letter": "စ္စ", "converts": ["စ်", "စ"]},
            {"row": 2, "column": 1, "doubleWith": 2, "consonant": "စ", "overlapped": "ဆ", "letter": "စ္ဆ", "converts": ["စ်", "ဆ"]},
            {"row": 2, "column": 3, "doubleWith": 1, "consonant": "ဇ", "overlapped": "ဇ", "letter": "ဇ္ဇ", "converts": ["ဇ်", "ဇ"]},
            {"row": 2, "column": 3, "doubleWith": 2, "consonant": "ဇ", "overlapped": "ၛ", "letter": "ဇ္ၛ", "converts": ["ဇ်", "ၛ"]},
            {"row": 2, "column": 5, "doubleWith": 5, "consonant": "ည", "overlapped": "ည", "letter": "ည", "converts": ["ည်", "ည"]},
            {"row": 2, "column": 5, "doubleWith": 1, "consonant": "ည", "overlapped": "စ", "letter": "ည္စ", "converts": ["ည်", "စ"]},
            {"row": 2, "column": 5, "doubleWith": 2, "consonant": "ည", "overlapped": "ဆ", "letter": "ည္ဆ", "converts": ["ည်", "ဆ"]},
            {"row": 2, "column": 5, "doubleWith": 3, "consonant": "ည", "overlapped": "ဇ", "letter": "ည္ဇ", "converts": ["ည်", "ဇ"]},
            {"row": 2, "column": 5, "doubleWith": 4, "consonant": "ည", "overlapped": "ၛ", "letter": "ည္ၛ", "converts": ["ည်", "ၛ"]},
            # ROW-3
            {"row": 3, "column": 1, "doubleWith": 1, "consonant": "ဋ", "overlapped": "ဋ", "letter": "ဋ", "converts": ["ဋ်", "ဋ"]},
            {"row": 3, "column": 1, "doubleWith": 2, "consonant": "ဋ", "overlapped": "ဌ", "letter": "ဋ္ဌ", "converts": ["ဋ်", "ဌ"]},
            # letter ဍ is an exception (commented out in original)
            {"row": 3, "column": 3, "doubleWith": 4, "consonant": "ဍ", "overlapped": "ဎ", "letter": "ဍ္ဎ", "converts": ["ဍ်", "ဎ"]},
            {"row": 3, "column": 5, "doubleWith": 5, "consonant": "ဏ", "overlapped": "ဏ", "letter": "ဏ္ဏ", "converts": ["ဏ်", "ဏ"]},
            {"row": 3, "column": 5, "doubleWith": 1, "consonant": "ဏ", "overlapped": "ဋ", "letter": "ဏ္ဋ", "converts": ["ဏ်", "ဋ"]},
            {"row": 3, "column": 5, "doubleWith": 2, "consonant": "ဏ", "overlapped": "ဌ", "letter": "ဏ္ဌ", "converts": ["ဏ်", "ဌ"]},
            {"row": 3, "column": 5, "doubleWith": 3, "consonant": "ဏ", "overlapped": "ဍ", "letter": "ဏ္ဍ", "converts": ["ဏ်", "ဍ"]},
            {"row": 3, "column": 5, "doubleWith": 4, "consonant": "ဏ", "overlapped": "ဎ", "letter": "ဏ္ဎ", "converts": ["ဏ်", "ဎ"]},
            # ROW-4
            {"row": 4, "column": 1, "doubleWith": 1, "consonant": "တ", "overlapped": "တ", "letter": "တ္တ", "converts": ["တ်", "တ"]},
            {"row": 4, "column": 1, "doubleWith": 2, "consonant": "တ", "overlapped": "ထ", "letter": "တ္ထ", "converts": ["တ်", "ထ"]},
            {"row": 4, "column": 3, "doubleWith": 3, "consonant": "ဒ", "overlapped": "ဒ", "letter": "ဒ္ဒ", "converts": ["ဒ်", "ဒ"]},
            {"row": 4, "column": 3, "doubleWith": 4, "consonant": "ဒ", "overlapped": "ဓ", "letter": "ဒ္ဓ", "converts": ["ဒ်", "ဓ"]},
            {"row": 4, "column": 5, "doubleWith": 5, "consonant": "န", "overlapped": "န", "letter": "န္န", "converts": ["န်", "န"]},
            {"row": 4, "column": 5, "doubleWith": 1, "consonant": "န", "overlapped": "တ", "letter": "န္တ", "converts": ["န်", "တ"]},
            {"row": 4, "column": 5, "doubleWith": 2, "consonant": "န", "overlapped": "ထ", "letter": "န္ထ", "converts": ["န်", "ထ"]},
            {"row": 4, "column": 5, "doubleWith": 3, "consonant": "န", "overlapped": "ဒ", "letter": "န္ဒ", "converts": ["န်", "ဒ"]},
            {"row": 4, "column": 5, "doubleWith": 4, "consonant": "န", "overlapped": "ဓ", "letter": "န္ဓ", "converts": ["န်", "ဓ"]},
            # ROW-5
            {"row": 5, "column": 1, "doubleWith": 1, "consonant": "ပ", "overlapped": "ပ", "letter": "ပ္ပ", "converts": ["ပ်", "ပ"]},
            {"row": 5, "column": 1, "doubleWith": 2, "consonant": "ပ", "overlapped": "ဖ", "letter": "ပ္ဖ", "converts": ["ပ်", "ဖ"]},
            {"row": 5, "column": 3, "doubleWith": 3, "consonant": "ဗ", "overlapped": "ဗ", "letter": "ဗ္ဗ", "converts": ["ဗ်", "ဗ"]},
            {"row": 5, "column": 3, "doubleWith": 4, "consonant": "ဗ", "overlapped": "ဘ", "letter": "ဗ္ဘ", "converts": ["ဗ်", "ဘ"]},
            {"row": 5, "column": 5, "doubleWith": 5, "consonant": "မ", "overlapped": "မ", "letter": "မ္မ", "converts": ["မ်", "မ"]},
            {"row": 5, "column": 5, "doubleWith": 1, "consonant": "မ", "overlapped": "ပ", "letter": "မ္ပ", "converts": ["မ်", "ပ"]},
            {"row": 5, "column": 5, "doubleWith": 2, "consonant": "မ", "overlapped": "ဖ", "letter": "မ္ဖ", "converts": ["မ်", "ဖ"]},
            {"row": 5, "column": 5, "doubleWith": 3, "consonant": "မ", "overlapped": "ဗ", "letter": "မ္ဗ", "converts": ["မ်", "ဗ"]},
            {"row": 5, "column": 5, "doubleWith": 4, "consonant": "မ", "overlapped": "ဘ", "letter": "မ္ဘ", "converts": ["မ်", "ဘ"]},
            # ZERO-CONSONANT
            {"row": 6, "column": 1, "doubleWith": 1, "consonant": "ယ", "overlapped": "ယ", "compound": "ျ", "letter": "ယျ", "converts": ["ယ်", "ယ"]},
            {"row": 6, "column": 1, "doubleWith": 2, "consonant": "ယ", "overlapped": "ရ", "compound": "ြ", "letter": "ယြ", "converts": ["ယ်", "ရ"]},
            {"row": 6, "column": 3, "doubleWith": 3, "consonant": "လ", "overlapped": "လ", "letter": "လ္လ", "converts": ["လ်", "လ"]},
            {"row": 6, "column": 5, "doubleWith": 5, "consonant": "သ", "overlapped": "သ", "letter": "ဿ", "converts": ["သ်", "သ"]},
        ]

        self.doubleSymbol = "္"

    def get_example_direct(self):
        return self.exampleDirect

    def get_example_pali_sansakrit(self):
        return self.examplePaliSansakrit

    def get_by_doubled(self, doubled):
        return next((item for item in self.paliSansakrits if item.get("letter") == doubled), None)

    def get_by_pali_sansakrit(self, overlapping, overlapped):
        return next(
            (item for item in self.paliSansakrits if item.get("consonant") == overlapping and item.get("overlapped") == overlapped),
            None,
        )

    def get_by_pali_sansakrit2(self, overlapping, overlapped):
        # looks up by 'compound' field in original JS
        return next(
            (item for item in self.paliSansakrits if item.get("consonant") == overlapping and item.get("compound") == overlapped),
            None,
        )

    def is_double_consonant(self, doubled):
        return self.get_by_doubled(doubled) is not None

    def is_double_consonant2(self, overlapping, overlapped):
        return self.get_by_pali_sansakrit(overlapping, overlapped) is not None

    def is_double_symbol(self, symbol):
        return symbol == self.doubleSymbol
