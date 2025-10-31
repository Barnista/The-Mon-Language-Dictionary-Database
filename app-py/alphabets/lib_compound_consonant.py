class LibCompoundConsonant:
    def __init__(self):
        self.compound_consonants = [
            {
                'letter': 'ၚ',
                'tone': 'breathy',
                'ipa': 'ŋɛ̤ˀ',
                'th': 'เงี่ยะ',
                'thLetter': 'ง',
                'compoundIPA': 'ŋ',
                'compoundTH': 'ง',
                'compound': '္ၚ',
                'example': 'က + -္ၚ + = က္ၚ',
                'exampleIPA': 'kaˀŋaˀ',
                'exampleTH': 'กะงะ',
                'compoundWith': ['က', 'တ', 'ဒ', 'ပ', 'ဗ', 'မ', 'လ', 'သ', 'အ'],
            },
            {
                'letter': 'ည',
                'tone': 'breathy',
                'ipa': 'ɲɛ̤ˀ',
                'th': 'เญียะ',
                'thLetter': 'ญ',
                'compoundIPA': 'ɲ',
                'compoundTH': 'ญ',
                'compound': '္ည',
                'example': 'က + -္ည + = က္ည',
                'exampleIPA': 'kaˀɲaˀ',
                'exampleTH': 'กะญะ',
                'compoundWith': ['က', 'ဂ', 'ဒ', 'ပ'],
            },
            {
                'letter': 'ဍ',
                'tone': 'clear',
                'ipa': 'ɗaˀ',
                'th': 'ดะ',
                'thLetter': 'ฑ',
                'compoundIPA': 'ɗ',
                'compoundTH': 'ด',
                'compound': '္ဍ',
                'example': 'က + -္ဍ + = က္ဍ',
                'exampleIPA': 'kaˀɗaˀ',
                'exampleTH': 'กะดะ',
                'compoundWith': ['က', 'ခ', 'စ', 'ပ', 'ဖ', 'သ'],
            },
            {
                'letter': 'န',
                'tone': 'breathy',
                'ipa': 'nɛ̤ˀ',
                'th': 'เนียะ',
                'thLetter': 'น',
                'compoundIPA': 'n',
                'compoundTH': 'น',
                'compound': 'ၞ',
                'example': 'က + -ၞ + = ကၞ',
                'exampleIPA': 'kaˀnaˀ',
                'exampleTH': 'กะนะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'မ',
                'tone': 'breathy',
                'ipa': 'mɛ̤ˀ',
                'th': 'เมียะ',
                'thLetter': 'ม',
                'compoundIPA': 'm',
                'compoundTH': 'ม',
                'compound': 'ၟ',
                'example': 'က + -ၟ + = ကၟ',
                'exampleIPA': 'kaˀmaˀ',
                'exampleTH': 'กะมะ',
                'compoundWith': ['က', 'ခ', 'စ', 'ပ', 'ဖ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ', 'လ'],
            },
            {
                'letter': 'ယ',
                'tone': 'breathy',
                'ipa': 'jɛ̤ˀ',
                'th': 'เยียะ',
                'thLetter': 'ย',
                'compoundIPA': 'j',
                'compoundTH': 'ย',
                'compound': 'ျ',
                'example': 'က + -ျ + = ကျ',
                'exampleIPA': 'kjaˀ',
                'exampleTH': 'กยะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ရ',
                'tone': 'breathy',
                'ipa': 'rɛ̤ˀ',
                'th': 'เรียะ',
                'thLetter': 'ร',
                'compoundIPA': 'r',
                'compoundTH': 'ร',
                'compound': 'ြ',
                'example': 'က + -ြ + = ကြ',
                'exampleIPA': 'kraˀ',
                'exampleTH': 'กระ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'လ',
                'tone': 'breathy',
                'ipa': 'lɛ̤ˀ',
                'th': 'เลียะ',
                'thLetter': 'ล',
                'compoundIPA': 'l',
                'compoundTH': 'ล',
                'compound': 'ၠ',
                'example': 'က + -ၠ + = ကၠ',
                'exampleIPA': 'klaˀ',
                'exampleTH': 'กละ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ဝ',
                'tone': 'breathy',
                'ipa': 'wɛ̤ˀ',
                'th': 'เวียะ',
                'thLetter': 'ว',
                'compoundIPA': 'w',
                'compoundTH': 'ว',
                'compound': 'ွ',
                'example': 'က + -ွ + = ကွ',
                'exampleIPA': 'kwaˀ',
                'exampleTH': 'กวะ',
                'compoundWith': ['က', 'ခ', 'ဂ', 'စ', 'ဆ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ', 'မ', 'သ'],
            },
            {
                'letter': 'ဟ',
                'tone': 'clear',
                'ipa': 'haˀ',
                'th': 'ฮะ',
                'thLetter': 'ฮ',
                'compoundIPA': 'h',
                'compoundTH': 'ฮ',
                'compound': 'ှ',
                'example': 'ည + -ှ = ညှ',
                'exampleIPA': 'hɲaˀ',
                'exampleTH': 'ฮญะ',
                'compoundWith': ['ည', 'ဏ', 'မ', 'န', 'ယ', 'ရ', 'လ', 'ဝ'],
            },
            {
                'letter': 'ၜ',
                'tone': 'clear',
                'ipa': 'ɓaˀ',
                'th': 'บะ',
                'thLetter': 'บ',
                'compoundIPA': 'ɓ',
                'compoundTH': 'บ',
                'compound': '္ၜ',
                'example': 'က + -္ၜ = က္ၜ',
                'exampleIPA': 'kaˀɓaˀ',
                'exampleTH': 'กะบะ',
                'compoundWith': ['က', 'စ', 'တ', 'ထ', 'ဗ'],
            },
        ]

    def get_all(self):
        return self.compound_consonants

    def get_by_compound(self, compound):
        return next(
            (row for row in self.compound_consonants 
             if row["compound"] == compound or row["letter"] == compound),
            None
        )

    def get_by_overlaps(self, overlapping, overlapped):
        return next(
            (row for row in self.compound_consonants 
             if overlapping in row["compoundWith"] and row["letter"] == overlapped),
            None
        )

    def is_compound_consonant(self, compound):
        consonant = self.get_by_compound(compound)
        return bool(consonant)

    def is_compound_consonant2(self, overlapping, overlapped):
        consonant = self.get_by_overlaps(overlapping, overlapped)
        return bool(consonant)

    def plots(self):
        return self.compound_consonants

