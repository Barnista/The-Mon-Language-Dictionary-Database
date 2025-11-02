class LibVowel:
    def __init__(self):
        self.vowels = [
            {
                'letter': 'အ',
                'compound': '',
                'ipaCL': 'ʔa',
                'ipaBT': 'ʔɛˑa',
                'thCL': '-ะ',
                'thBT': 'แ-ฺ.',
            },
            {
                'letter': 'အာ',
                'compound': 'ာ',
                'compound2': 'ါ',
                'ipaCL': 'ʔaː',
                'ipaBT': 'ʔɛaː',
                'thCL': '-า',
                'thBT': 'แ-ฺ—า',
                'exception': {
                    'id': 'vowel-exception-1',
                    'dependsOnFinal': False,
                    'consonants': ['ခ', 'ဂ', 'ဇ', 'ဎ', 'ဒ', 'ပ', 'ဝ', 'ၜ']
                }
            },
            {
                'letter': 'ဣ',
                'compound': 'ိ',
                'ipaCL': 'ʔɒi',
                'ipaCL2': 'ʔɒi',
                'ipaBT': 'ʔì',
                'thCL': '-็อฺย',
                'thCL2': '-็อฺย',
                'thBT': '-ิ',
            },
            {
                'letter': 'ဣဳ',
                'compound': 'ဳ',
                'ipaCL': 'ʔɒːi',
                'ipaCL2': 'ʔɒːi',
                'ipaBT': 'ʔìː',
                'thCL': '-อฺย',
                'thCL2': '-อฺย',
                'thBT': '-ี่',
            },
            {
                'letter': 'ဥ',
                'compound': 'ု',
                'ipaCL': 'ʔau',
                'ipaCL2': 'ʔau',
                'ipaBT': 'ʔù',
                'thCL': 'เ-็า',
                'thCL2': 'เ-็า',
                'thBT': '-ุ',
            },
            {
                'letter': 'ဥူ',
                'compound': 'ူ',
                'ipaCL': 'ʔaːu',
                'ipaCL2': 'ʔaːu',
                'ipaBT': 'ʔùː',
                'thCL': 'เ-า',
                'thCL2': 'เ-า',
                'thBT': '-ู่',
            },
            {
                'letter': 'ဨ',
                'compound': 'ေ',
                'ipaCL': 'ʔeː',
                'ipaBT': 'ʔèː',
                'thCL': 'เ-',
                'thBT': 'เ-่',
            },
            {
                'letter': 'အဲ',
                'compound': 'ဲ',
                'ipaCL': 'ʔuːa',
                'ipaBT': 'ʔuːà',
                'thCL': '-ัว',
                'thBT': '-ั่ว',
            },
            {
                'letter': 'ဩ',
                'compound': 'ော',
                'compound2': 'ေါ',
                'ipaCL': 'ʔaːu',
                'ipaBT': 'ʔəː',
                'thCL': 'เ-า',
                'thBT': 'เ-่อ',
                'exception': {
                    'id': 'vowel-exception-2',
                    'dependsOnFinal': False,
                    'consonants': ['ခ', 'ဂ', 'ဇ', 'ဎ', 'ဒ', 'ပ', 'ဝ', 'ၜ']
                }
            },
            {
                'letter': 'အဴ‌‍‍',
                'compound': 'ဴ',
                'ipaCL': 'ʔaːw',
                'ipaBT': 'ʔɛaː',
                'thCL': '-าว',
                'thBT': 'แ-็—า',
            },
            {
                'letter': 'အံ',
                'compound': 'ံ',
                'ipaCL': 'ʔɔm',
                'ipaBT': 'ʔɔ̀m',
                'thCL': '-อม',
                'thBT': '-่อม',
            },
            {
                'letter': 'အး',
                'compound': 'း',
                'ipaCL': 'ʔah',
                'ipaBT': 'ʔɛh',
                'thCL': '-ะฮ',
                'thBT': 'แ-ฺฮ',
            }
        ]
        
        self.other_vowels = [
            {
                'letter': 'ို',
                'compound': 'ို',
                'ipaCL': 'ʔɒ',
                'ipaBT': 'ʔə̀',
                'thCL': 'เ-าฺะ',
                'thBT': 'เ-อะ',
                'origin': 'ိ + ု = ို',
            },
            {
                'letter': 'ာံ',
                'compound': 'ာံ',
                'ipaCL': 'ʔaːm',
                'ipaBT': 'ʔàːm',
                'thCL': '-าม',
                'thBT': '-่าม',
                'origin': 'ာ + မ် = ာံ',
            },
            {
                'letter': 'ုံ',
                'compound': 'ုံ',
                'ipaCL': 'ʔum',
                'ipaBT': 'ʔùm',
                'thCL': '-ุม',
                'thBT': '-ุ่ม',
                'origin': 'ု + မ် = ုံ'
            },
            {
                'letter': 'ေံ',
                'compound': 'ေံ',
                'ipaCL': 'ʔeːm',
                'ipaBT': 'ʔèːm',
                'thCL': 'เ-ม',
                'thBT': 'เ-่ม',
                'origin': 'ေ + မ် = ေံ <br>  ေ + အ် = ေံ'
            },
            {
                'letter': 'ောံ',
                'compound': 'ောံ',
                'ipaCL': 'ʔoːm',
                'ipaBT': 'ʔòːm',
                'thCL': 'โ-ม',
                'thBT': 'โ-่ม',
                'origin': 'ော + မ် = ောံ <br> ေါ + မ် = ေံါ'
            },
            {
                'letter': 'ီ',
                'compound': 'ီ',
                'ipaCL': 'ʔim',
                'ipaBT': 'ʔìm',
                'thCL': '-ิม',
                'thBT': '-ิ่ม',
                'origin': 'ိ + မ် = ီ'
            },
            {
                'letter': 'ီု',
                'compound': 'ီု',
                'ipaCL': 'ʔɒːm',
                'ipaBT': 'ʔə̀ːm',
                'thCL': '-าฺม',
                'thBT': 'เ-ิ่ม',
                'origin': 'ိ + ု + မ် = ီု'
            },
            {
                'letter': 'ာဲ',
                'compound': 'ာဲ',
                'compound2': 'ဲါ',
                'ipaCL': 'ʔaːj',
                'ipaBT': 'ʔàːj',
                'thCL': '-าย',
                'thBT': '-่าย',
                'origin': 'ာ + ယ် = ာဲ <br> ါ + ယ် = ဲါ'
            },
            {
                'letter': 'ုဲ',
                'compound': 'ုဲ',
                'ipaCL': 'ʔuj',
                'ipaBT': 'ʔùj',
                'thCL': '-ุย',
                'thBT': '-ุ่ย',
                'origin': 'ု + ယ် = ုဲ'
            },
            {
                'letter': 'ေဲ',
                'compound': 'ေဲ',
                'ipaCL': 'ʔiːa',
                'ipaBT': 'ʔiːà',
                'thCL': 'เ-ีย',
                'thBT': 'เ-ี่ย',
                'origin': 'ေ + ယ် = ေဲ'
            },
            {
                'letter': 'ောဲ',
                'compound': 'ောဲ',
                'compound2': 'ေဲါ',
                'ipaCL': 'ʔuːa',
                'ipaBT': 'ʔuːà',
                'thCL': '-ัว',
                'thBT': '-ั่ว',
                'origin': 'ော + ယ် = ောဲ <br> ေါ + ယ် = ေဲါ'
            },
            {
                'letter': 'ိုဲ',
                'compound': 'ိုဲ',
                'ipaCL': 'ʔəːj',
                'ipaBT': 'ʔə̀ːj',
                'thCL': 'เ-ย',
                'thBT': 'เ-่ย',
                'origin': 'ိ + ု + ယ် = ိုဲ'
            },
            {
                'letter': 'ဵု',
                'compound': 'ဵု',
                'ipaCL': 'ʔɒː',
                'ipaBT': 'ʔə̀ː',
                'thCL': '-ฺอ',
                'thBT': 'เ-่อ',
                'origin': 'ိ + ု + ဝ် = ဵု'
            }
        ]

    def get_all(self):
        return self.vowels

    def get_all_other_vowels(self):
        return self.other_vowels

    def get_by_letter(self, letter):
        return next((vowel for vowel in self.vowels if vowel['letter'] == letter), None)

    def get_by_compound(self, compound):
        # Check main vowels
        for vowel in self.vowels:
            if vowel.get('compound') == compound or vowel.get('compound2') == compound:
                return vowel
                
        # Check other vowels
        for vowel in self.other_vowels:
            if vowel.get('compound') == compound or vowel.get('compound2') == compound:
                return vowel
        
        return None

    def is_stand_alone_vowel(self, letter):
        return self.get_by_letter(letter) is not None

    def is_compound_vowel(self, compound):
        return self.get_by_compound(compound) is not None

    def plots(self):
        return self.vowels
