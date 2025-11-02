class LibRule:
    def __init__(self):
        self.rules = {
            'tones': {
                'clear': [
                    'က', 'ခ', 'စ', 'ဆ', 'ဋ', 'ဌ', 'ဍ', 'ဏ', 'တ', 'ထ', 'ပ', 'ဖ', 'သ', 'ဟ', 'ဠ', 'ၜ', 'အ'
                ],
                'breathy': [
                    'ဂ', 'ဃ', 'ၚ', 'ဇ', 'ၛ', 'ည', 'ဎ', 'ဒ', 'ဓ', 'န', 'ဗ', 'ဘ', 'မ', 'ယ', 'ရ', 'လ', 'ဝ', 'ၝ'
                ],
            },
            'blendVowels': [
                {
                    'vowel': 'ာ',
                    'replace': 'ါ',
                    'consonants': ['ခ', 'ဂ', 'ဇ', 'ဎ', 'ဒ', 'ပ', 'ဝ', 'ၜ']
                },
                {
                    'vowel': 'ါ',
                    'replace': 'ာ',
                    'consonants': [
                        'က', 'စ', 'ဆ', 'ဋ', 'ဌ', 'ဍ', 'ဏ', 'တ', 'ထ', 'ဓ', 'န', 'ဗ', 'ဘ', 'မ', 'ယ', 'ရ', 'လ', 'သ', 'ဟ', 'ဠ', 'ၛ', 'ည', 'ၝ', 'အ'
                    ]
                },
                {
                    'vowel': 'ော',
                    'replace': 'ေါ',
                    'consonants': ['ခ', 'ဂ', 'ဇ', 'ဎ', 'ဒ', 'ပ', 'ဝ', 'ၜ']
                },
                {
                    'vowel': 'ေါ',
                    'replace': 'ော',
                    'consonants': [
                        'က', 'စ', 'ဆ', 'ဋ', 'ဌ', 'ဍ', 'ဏ', 'တ', 'ထ', 'ဓ', 'န', 'ဗ', 'ဘ', 'မ', 'ယ', 'ရ', 'လ', 'သ', 'ဟ', 'ဠ', 'ၛ', 'ည', 'ၝ', 'အ'
                    ]
                },
            ],
            'blendCompounds': [
                {
                    'compound': 'ျ',
                    'letters': ['က', 'ခ', 'ဂ', 'ဇ', 'ပ', 'ဖ', 'ဗ'],
                },
                {
                    'compound': 'ြ',
                    'letters': ['က', 'ခ', 'ဂ', 'ဇ', 'တ', 'ထ', 'ဒ', 'ပ', 'ဖ', 'ဗ'],
                },
                {
                    'compound': 'ၠ',
                    'letters': ['က', 'ခ', 'ဂ', 'ပ', 'ဖ', 'ဗ'],
                },
                {
                    'compound': 'ွ',
                    'letters': ['က', 'ခ', 'ဂ', 'ဇ', 'ဘ'],
                },
                {
                    'compound': 'ှ',
                    'isReversed': True,
                    'letters': ['ည', 'ဏ', 'မ', 'န', 'ယ', 'ရ', 'လ', 'ဝ'],
                }
            ],
            'blendFinals': [
                {
                    'final': 'က်',
                    'final2': '်',
                    'vowels': [
                        {'vowel': 'ာ', 'replace': 'ာ်'},
                        {'vowel': 'ော', 'replace': 'ော်'},
                        {'vowel': 'ါ', 'replace': 'ါ်'},
                        {'vowel': 'ေါ', 'replace': 'ေါ်'},
                    ]
                },
                {
                    'final': 'မ်',
                    'final2': 'ံ',
                    'vowels': [
                        {'vowel': '', 'replace': 'ံ'},
                        {'vowel': 'ာ', 'replace': 'ာံ'},
                        {'vowel': 'ါ', 'replace': 'ံါ'},
                        {'vowel': 'ိ', 'replace': 'ီ'},
                        {'vowel': 'ု', 'replace': 'ုံ'},
                        {'vowel': 'ေ', 'replace': 'ေံ'},
                        {'vowel': 'ော', 'replace': 'ောံ'},
                        {'vowel': 'ေါ', 'replace': 'ေံါ'},
                        {'vowel': 'ို', 'replace': 'ီု'}
                    ]
                },
                {
                    'final': 'ယ်',
                    'final2': 'ဲ',
                    'vowels': [
                        {'vowel': '', 'replace': 'ဲ'},
                        {'vowel': 'ာ', 'replace': 'ာဲ'},
                        {'vowel': 'ါ', 'replace': 'ဲါ'},
                        {'vowel': 'ု', 'replace': 'ုဲ'},
                        {'vowel': 'ေ', 'replace': 'ေဲ'},
                        {'vowel': 'ော', 'replace': 'ောဲ'},
                        {'vowel': 'ေါ', 'replace': 'ေဲါ'},
                        {'vowel': 'ို', 'replace': 'ိုဲ'}
                    ]
                },
                {
                    'final': 'ဝ်',
                    'final2': 'ဵု',
                    'vowels': [
                        {'vowel': 'ို', 'replace': 'ဵု'}
                    ],
                },
                {
                    'final': 'ဟ်',
                    'final2': '်ှ',
                    'vowels': [
                        {'vowel': '', 'replace': '်ှ'},
                        {'vowel': 'ေ', 'replace': '်ှေ'},
                        {'vowel': 'ော', 'replace': '်ှော'},
                        {'vowel': 'ေါ', 'replace': '်ှော'}
                    ]
                },
                {
                    'final': 'အ်',
                    'final2': 'ံ',
                    'vowels': [
                        {'vowel': '', 'replace': 'ံ'},
                        {'vowel': 'ေ', 'replace': 'ေံ'},
                        {'vowel': 'ော', 'replace': 'ောံ'},
                        {'vowel': 'ေါ', 'replace': 'ေံါ'},
                    ],
                    'isLegacy': True
                }
            ],
            'blendTHs': [
                {'vowel': '-ะ', 'replace': '-ั'},
                {'vowel': 'เ-อ', 'replace': 'เ-ิ'},
                {'vowel': 'เ-่อ', 'replace': 'เ-ิ่'},
                {'vowel': 'โ-่ะ', 'replace': '-่'},
            ],
        }

    def get_all(self):
        return self.rules

    def is_breathy_consonant(self, letter):
        return letter in self.rules['tones']['breathy']

    def is_clear_consonant(self, letter):
        return letter in self.rules['tones']['clear']

    def find_blend_vowel(self, vowel_compound, consonant):
        return next((rule for rule in self.rules['blendVowels'] 
                     if rule['vowel'] == vowel_compound and consonant in rule['consonants']), None)

    def find_blend_compound(self, compound, consonant):
        return next((c for c in self.rules['blendCompounds'] 
                     if c['compound'] == compound and consonant in c['letters']), None)

    def find_blend_final(self, final):
        return next((blend for blend in self.rules['blendFinals'] 
                     if blend['final'] == final or blend['final2'] == final), None)

    def find_blend_th(self, vowel):
        return next((rule for rule in self.rules['blendTHs'] 
                     if rule['vowel'] == vowel), None)
    
    # Exceptional rules for blend compounds NOTICED BY Mr.Zuzarz
    def find_blend_compound_exceptional(self, consonant, compound, vowel, final_consonant):
        # Consonant + Compound exceptional rules
        if consonant == 'က' and compound == 'ျ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ခ' and compound == 'ျ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ဂ' and compound == 'ျ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': True,
            }
        if consonant == 'ဖ' and compound == 'ျ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'စ' and compound == 'ြ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ဇ' and compound == 'ြ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': True,
            }
        if consonant == 'သ' and compound == 'ြ':
            # သ +  ြ  = "s" sound
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'တ' and compound == 'ြ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ဒ' and compound == 'ြ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': True,
            }
        if consonant == 'သ' and compound == 'ၠ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ဇ' and compound == 'ွ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': True,
            }
        if consonant == 'တ' and compound == 'ွ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'သ' and compound == 'ွ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'သ' and compound == '္ၚ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ဇ' and compound == '္ၚ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': True,
            }
        if consonant == 'သ' and compound == '္ဇ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ရ' and compound == 'ှ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        if consonant == 'ည' and compound == 'ှ':
            return {
                'consonant': consonant+compound,
                'compound': '',
                'vowel': vowel,
                'final_consonant': final_consonant,
                'is_breathy': False,
            }
        # Compound + Final consonant exceptional rules
        if compound == 'ွ' and vowel == '' and final_consonant == 'မ်':
            return {
                'consonant': consonant,
                'compound': '',
                'vowel': 'ို',
                'final_consonant': final_consonant,
            }
        elif compound == 'ွ' and vowel == '' and final_consonant == 'ယ်':
            # for example မွဲ
            return {
                'consonant': consonant,
                'compound': '',
                'vowel': '',
                'final_consonant': final_consonant,
            }
        
        return None
