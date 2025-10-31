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
                'ipaCL': 'ɒ',
                'ipaBT': 'ə̤',
                'ipaBT2': 'a̤',
                'thCL': '-าฺ',
                'thBT': '-่าฺ',
                'thBT2': '-่าฺ',
                'origin': 'ိ + ု = ို',
            },
            {
                'letter': 'ာံ',
                'compound': 'ာံ',
                'ipaCL': 'am',
                'ipaBT': 'èm',
                'thCL': '-าม',
                'thBT': 'เ-่ม',
                'origin': 'ာ + မ် = ာံ',
            },
            {
                'letter': 'ုံ',
                'compound': 'ုံ',
                'ipaCL': 'um',
                'ipaBT': 'ùm',
                'thCL': '-ุม',
                'thBT': '-ุ่ม',
                'origin': 'ု + မ် = ုံ'
            },
            {
                'letter': 'ေံ',
                'compound': 'ေံ',
                'ipaCL': 'em',
                'ipaCL2': 'eˀ',
                'ipaCL3': 'eh',
                'ipaBT': 'èm',
                'ipaBT2': 'èˀ',
                'thCL': 'เ-ม',
                'thCL2': 'เ-ะ',
                'thCL3': 'เ-ะ',
                'thBT': 'เ-่ม',
                'thBT2': 'เ-่ะ',
                'origin': 'ေ + မ် = ေံ <br>  ေ + အ် = ေံ'
            },
            {
                'letter': 'ောံ',
                'compound': 'ောံ',
                'ipaCL': 'om',
                'ipaCL2': 'ò',
                'ipaBT': 'òm',
                'ipaBT2': 'òˀ',
                'thCL': 'โ-ม',
                'thCL2': 'โ-ะ',
                'thBT': 'โ-่ม',
                'thBT2': 'โ-่ะ',
                'origin': 'ော + မ် = ောံ <br> ေါ + မ် = ေံါ'
            },
            {
                'letter': 'ီ',
                'compound': 'ီ',
                'ipaCL': 'ɔeˀm',
                'ipaBT': 'ìˀm',
                'thCL': '-ิม',
                'thBT': '-ิ่ม',
                'origin': 'ိ + မ် = ီ'
            },
            {
                'letter': 'ီု',
                'compound': 'ီု',
                'ipaCL': 'ɒm',
                'ipaBT': 'ɤˀm',
                'thCL': '-อฺม',
                'thBT': 'เ-ิ่ม',
                'origin': 'ိ + ု + မ် = ီု'
            },
            {
                'letter': 'ာဲ',
                'compound': 'ာဲ',
                'compound2': 'ဲါ',
                'ipaCL': 'ai',
                'ipaBT': 'a̤i',
                'thCL': '-าย',
                'thBT': '-่าย',
                'origin': 'ာ + ယ် = ာဲ <br> ါ + ယ် = ဲါ'
            },
            {
                'letter': 'ုဲ',
                'compound': 'ုဲ',
                'ipaCL': 'ui',
                'ipaBT': 'ùi',
                'thCL': '-ุย',
                'thBT': '-ุ่ย',
                'origin': 'ု + ယ် = ုဲ'
            },
            {
                'letter': 'ေဲ',
                'compound': 'ေဲ',
                'ipaCL': 'ea',
                'ipaBT': 'ɛ̀a',
                'thCL': 'เ-ีย',
                'thBT': 'เ-ี่ย',
                'origin': 'ေ + ယ် = ေဲ'
            },
            {
                'letter': 'ောဲ',
                'compound': 'ောဲ',
                'compound2': 'ေဲါ',
                'ipaCL': 'oa',
                'ipaBT': 'òa',
                'thCL': '-ัว',
                'thBT': '-ั่ว',
                'origin': 'ော + ယ် = ောဲ <br> ေါ + ယ် = ေဲါ'
            },
            {
                'letter': 'ိုဲ',
                'compound': 'ိုဲ',
                'ipaCL': 'ɤi',
                'ipaCL2': 'oi',
                'ipaBT': 'ɤiˀ',
                'thCL': 'เ-ย',
                'thCL2': 'โ-ย',
                'thBT': 'เ-่ย',
                'origin': 'ိ + ု + ယ် = ိုဲ'
            },
            {
                'letter': 'ဵု',
                'compound': 'ဵု',
                'ipaCL': 'ɒw',
                'ipaBT': 'ɤˀw',
                'thCL': '-อฺว',
                'thBT': 'เ-ิ่ว',
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
