class LibNumeral:
    def __init__(self):
        self.numbers = [
            {
                'number': 0,
                'digit': 1,
                'letter': '၀',
                'thLetter': '๐',
                'spelling': 'သုည',
                'ipa': 'suɲɲa',
                'th': 'ซุญ-ญะ'
            },
            {
                'number': 1,
                'digit': 1,
                'letter': '၁',
                'thLetter': '๑',
                'spelling': 'မွဲ',
                'ipa': 'mṳa',
                'th': 'มัว'
            },
            {
                'number': 2,
                'digit': 1,
                'letter': '၂',
                'thLetter': '๒',
                'spelling': 'ၜါ',
                'ipa': 'ɓa',
                'th': 'บา'
            },
            {
                'number': 3,
                'digit': 1,
                'letter': '၃',
                'thLetter': '๓',
                'spelling': 'ပိ',
                'ipa': 'pɔɪ',
                'th': 'ปอฺย'
            },
            {
                'number': 4,
                'digit': 1,
                'letter': '၄',
                'thLetter': '๔',
                'spelling': 'ပန်',
                'ipa': 'pɒn',
                'th': 'ปอน'
            },
            {
                'number': 5,
                'digit': 1,
                'letter': '၅',
                'thLetter': '๕',
                'spelling': 'မသုန်',
                'ipa': 'mɛ̀ˀ-sùˀn',
                'th': 'เมี่ยะ-ซุน',
                'spelling2': 'သုန်',
                'ipa2': 'sùˀn',
                'th2': 'ซุน',
            },
            {
                'number': 6,
                'digit': 1,
                'letter': '၆',
                'thLetter': '๖',
                'spelling': 'တရဴ',
                'ipa': 'taˀ-roa',
                'th': 'ตะ-ราว'
            },
            {
                'number': 7,
                'digit': 1,
                'letter': '၇',
                'thLetter': '๗',
                'spelling': 'ထပှ်',
                'ipa': 'tʰaˀ-pɒh',
                'th': 'ทะ-ปอฮ',
            },
            {
                'number': 8,
                'digit': 1,
                'letter': '၈',
                'thLetter': '๘',
                'spelling': 'ဒစာံ',
                'ipa': 'tɛ̀ˀcam',
                'th': 'เตี่ยะ-จาม',
            },
            {
                'number': 9,
                'digit': 1,
                'letter': '၉',
                'thLetter': '๙',
                'spelling': 'ဒစိတ်',
                'ipa': 'tɛ̀ˀ-cɔeˀt',
                'th': 'เตี่ยะ-จิด',
            },
            {
                'number': 10,
                'digit': 2,
                'letter': '၁၀',
                'thLetter': '๑๐',
                'spelling': 'စှ်',
                'ipa': 'cɒh',
                'th': 'จอฮ',
            },
            {
                'number': 100,
                'digit': 3,
                'letter': '၁၀၀',
                'thLetter': '๑๐๐',
                'spelling': 'ကၠံ',
                'ipa': 'klɒm',
                'th': 'กลอม',
            },
            {
                'number': 1000,
                'digit': 4,
                'letter': '၁၀၀၀',
                'thLetter': '๑,๐๐๐',
                'spelling': 'လ္ၚီ',
                'ipa': 'lɛ̤ˀŋìˀm',
                'th': 'เลียะงิ่ม',
            },
            {
                'number': 10000,
                'digit': 5,
                'letter': '၁၀၀၀၀',
                'thLetter': '๑๐,๐๐๐',
                'spelling': 'လှက်',
                'ipa': 'laˀk',
                'th': 'ลัก',
            },
            {
                'number': 100000,
                'digit': 6,
                'letter': '၁၀၀၀၀၀',
                'thLetter': '๑๐๐,๐๐๐',
                'spelling': 'ကိုတ်',
                'ipa': 'kɒt',
                'th': 'กอฺด',
            },
            {
                'number': 1000000,
                'digit': 7,
                'letter': '၁၀၀၀၀၀၀',
                'thLetter': '๑,๐๐๐,๐๐๐',
                'spelling': 'ပြကောတိကိုတ်',
                'ipa': 'praˀ-kao-tɔɪ-kɒt',
                'th': 'ประ-เกา-ตอฺย-กอฺด',
            },
            {
                'number': 10000000,
                'digit': 8,
                'letter': '၁၀၀၀၀၀၀၀',
                'thLetter': '๑๐,๐๐๐,๐๐๐',
                'spelling': 'နိလဟုတ်',
                'ipa': 'nìˀ-lɛ̀ˀ-hùˀt',
                'th': 'นิ่-เลี่ยะ-ฮุด',
            },
            {
                'number': 100000000,
                'digit': 9,
                'letter': '၁၀၀၀၀၀၀၀၀',
                'thLetter': '๑๐๐,๐๐๐,๐๐๐',
                'spelling': 'နိလဟုတ်တံင်',
                'ipa': 'nìˀ-lɛ̀ˀ-hùˀt-tɒŋ',
                'th': 'นิ่-เลี่ยะ-ฮุด-ตอง',
            },
            {
                'number': 1000000000,
                'digit': 10,
                'letter': '၁၀၀၀၀၀၀၀၀၀',
                'thLetter': '๑,๐๐๐,๐๐๐,๐๐๐',
                'spelling': 'အသင်ဃဲယံင်',
                'ipa': 'ʔaˀ-saˀŋ-kʰòa-jɒˀŋ',
                'th': 'อะ-ซัง-คั่ว-ย่อง',
            }
        ]
        self.examples = [
            {
                'number': 11,
                'digit': 2,
                'letter': '၁၁',
                'thLetter': '๑๑',
                'spelling': 'စှ်-မွဲ',
                'ipa': 'cɒh-mṳa',
                'th': 'จอฮ-มัว'
            },
            {
                'number': 15,
                'digit': 2,
                'letter': '၁၅',
                'thLetter': '๑๕',
                'spelling': 'စှ်-သုန်',
                'ipa': 'cɒh-sùˀn',
                'th': 'จอฮ-ซุน'
            },
            {
                'number': 20,
                'digit': 2,
                'letter': '၂၀',
                'thLetter': '๒๐',
                'spelling': 'ၜါ-စှ်',
                'ipa': 'ɓa-cɒh',
                'th': 'บา-จอฮ'
            },
            {
                'number': 158,
                'digit': 3,
                'letter': '၁၅၈',
                'thLetter': '๑๕๘',
                'spelling': 'ကၠံ-မသုန်-စှ်-ဒစာံ',
                'ipa': 'klɒm-mɛ̀ˀ-sùˀn-cɒh-tɛ̀ˀcam',
                'th': 'กลอม-เมี่ยะ-ซุน-จอฮ-เตี่ยะ-จาม'
            },
            {
                'number': 500,
                'digit': 3,
                'letter': '၅၀၀',
                'thLetter': '๕๐๐',
                'spelling': 'မသုန်-ကၠံ',
                'ipa': 'mɛ̀ˀ-sùˀn-klɒm',
                'th': 'เมี่ยะ-ซุน-กลอม'
            },
            {
                'number': 9999,
                'digit': 4,
                'letter': '၉၉၉၉',
                'thLetter': '๙,๙๙๙',
                'spelling': 'ဒစိတ်-လ္ၚီ-ဒစိတ်-ကၠံ-ဒစိတ်-စှ်-ဒစိတ်',
                'ipa': 'tɛ̀ˀ-cɔeˀt-lɛ̤ˀŋìˀm-tɛ̀ˀ-cɔeˀt-klɒm-tɛ̀ˀ-cɔeˀt-cɒh-tɛ̀ˀ-cɔeˀt',
                'th': 'เตี่ยะ-จิด-เลียะงิ่ม-เตี่ยะ-จิด-กลอม-เตี่ยะ-จิด-จอฮ-เตี่ยะ-จิด',
            },
            {
                'number': 60205,
                'digit': 5,
                'letter': '၆၀၂၀၅',
                'thLetter': '๖๐,๒๐๕',
                'spelling': 'တရဴ-လှက်-ၜါ-ကၠံ-သုန်',
                'ipa': 'taˀ-roa-laˀk-ɓa-klɒm-sùˀn',
                'th': 'ตะ-ราว-ลัก-บา-กลอม-ซุน'
            }
        ]
        self.decimalExamples = [
            {
                'number': 7.5,
                'digit': 1,
                'letter': "၇.၅",
                'spelling': "ထပှ်-ဒဿမ-မသုန်",
                'ipa': 'tʰaˀ-pɒh-tòs-saˀ-mɛ̀ˀ-mɛ̀ˀ-sùˀn',
                'th': 'ทะ-ปอฮ-ต่ซ-ซะ-เมี่ยะ-เมี่ยะ-ซุน'
            },
            {
                'number': 1.843,
                'digit': 1,
                'letter': "၁.၈၄၃",
                'spelling': "မွဲ-ဒဿမ-ဒစာံ-ပန်-ပိ",
                'ipa': 'mṳa-tòs-saˀ-mɛ̀ˀ-tɛ̀ˀcam-pɒn-pɔɪ',
                'th': 'มัว-ต่ซ-ซะ-เมี่ยะ-เตี่ยะ-จาม-ปอน-ปอฺย'
            },
            {
                'number': 50.98,
                'digit': 2,
                'letter': "၅၀.၉၈",
                'spelling': "မသုန်စှ်-ဒဿမ-ဒစိတ်-ဒစာံ",
                'ipa': "mɛ̀ˀ-sùˀn-cɒh-tòs-saˀ-mɛ̀ˀ-tɛ̀ˀ-cɔeˀt-tɛ̀ˀcam",
                'th': "เมี่ยะ-ซุน-จอฮ-ต่ซ-ซะ-เมี่ยะ-เตี่ยะ-จิด-เตี่ยะ-จาม"
            }
        ]
        self.equationExamples = [
            {
                'equation': "၁ + ၂ = ၃",
                'equation2': "1 + 2 = 3",
                'spelling': "မွဲ-ဟုဲ-ၜါ-တုပ်သၟဟ်-ပိ",
                'ipa': "mṳa-hùi-ɓa-tùˀp-saˀmɒh-pɔɪ",
                'th': "มัว-ฮุย-บา-ตุบ-ซะมอฮ-ปอฺย",
            },
            {
                'equation': "၁၉ - ၄ = ၁၅",
                'equation2': "19 - 4 = 15",
                'spelling': "စှ်-ဒစိတ်-နုက်-ပန်-တုပ်သၟဟ်-စှ်-သုန်",
                'ipa': "cɒh-tɛ̀ˀ-cɔeˀt-nɤˀk-pɒn-tùˀp-saˀmɒh-cɒh-sùˀn",
                'th': "จอฮ-เตี่ยะ-จิด-เนิ่ก-ปอน-ตุบ-ซะมอฮ-จอฮ-ซุน",
            },
            {
                'equation': "၈ × ၄ = ၃၂",
                'equation2': "8 × 4 = 32",
                'spelling': "မွဲ-ပၟဝ်-ပန်-တုပ်သၟဟ်-ပိစှ်-ၜါ",
                'ipa': "mṳa-paˀmɒw-pɒn-tùˀp-saˀmɒh-pɔɪ-cɒh-ɓa",
                'th': "มัว-ปะมอว-ปอน-ตุบ-ซะมอฮ-ปอฺย-จอฮ-บา",
            },
            {
                'equation': "၇၂ ÷ ၁၂ = ၆",
                'equation2': "72 ÷ 12 = 6",
                'spelling': "ထပှ်စှ်-ၜါ-စ-စှ်-ၜါ-တုပ်သၟဟ်-တရဴ",
                'ipa': "tʰaˀ-pɒh-cɒh-ɓa-caˀ-cɒh-ɓa-tùˀp-saˀmɒh-taˀ-roa",
                'th': "ทะ-ปอฮ-จอฮ-บา-จะ-จอฮ-บา-ตุบ-ซะมอฮ-ตะ-ราว",
            }
        ]
        self.symbols = [
            {
                'letter': ".",
                'spelling': "ဒဿမ",
                'spelling2': "ဒသ္သမ",
                'ipa': 'tòs-saˀ-mɛ̀ˀ',
                'th': 'ต่ซ-ซะ-เมี่ยะ'
            },
            {
                'letter': "+",
                'spelling': "ဟုယ်",
                'spelling2': "ဟုဲ",
                'ipa': "hùi",
                'th': "ฮุย"
            },
            {
                'letter': "-",
                'spelling': "နုက်",
                'ipa': "nɤˀk",
                'th': "เนิ่ก"
            },
            {
                'letter': "×",
                'letter2': "*",
                'spelling': "ပၟဝ်",
                'ipa': "paˀmɒw",
                'th': "ปะมอว"
            },
            {
                'letter': "÷",
                'letter2': "/",
                'spelling': "စ",
                'ipa': "caˀ",
                'th': "จะ"
            },
            {
                'letter': "=",
                'spelling': "တုပ်သၟဟ်",
                'spelling2': "ညဳ",
                'ipa': "tùˀp-saˀmɒh",
                'th': "ตุบ-ซะมอฮ",
                'ipa2': "ɲì",
                'th2': "ญี่"
            }
        ]

    def is_symbol(self, symbol):
        return symbol == '.' or symbol == ','
    
    def is_number_char(self, num):
        num1 = next((val for val in self.numbers if val['letter'] == num), None)
        num2 = num.isdigit()
        return bool(num1 or num2)
    
    def get_number(self, num):
        try:
            arabic = float(num)
            return self.convert_from_arabic(str(arabic), False)
        except ValueError:
            mon = self.convert_from_mon(str(num), False)
            if mon['arabicNum'] != '':
                return mon
            return None
    
    def mon_to_arabic(self, mon_number_str, include_comma):
        result = ''
        
        if mon_number_str:
            str_chars = list(str(mon_number_str))
            num_str = ''
            for char in str_chars:
                num_item = next((val for val in self.numbers if val['letter'] == char), None)
                if num_item:
                    num_str += str(num_item['number'])
                elif char == '.':
                    num_str += char
            
            result = num_str
        
        return result
    
    def arabic_to_mon(self, arabic_number_str):
        result = ''
        
        if arabic_number_str:
            str_chars = list(str(arabic_number_str))
            num_str = ''
            for char in str_chars:
                num_item = next((val for val in self.numbers if str(val['number']) == char), None)
                if num_item:
                    num_str += num_item['letter']
                elif char == '.':
                    num_str += char
            
            result = num_str
        
        return result
    
    def mon_to_thai(self, mon_number_str, include_comma):
        result = ''

        if mon_number_str:
            str_chars = list(str(mon_number_str))
            num_str = ''
            for char in str_chars:
                num_item = next((val for val in self.numbers if val['letter'] == char), None)
                if num_item:
                    num_str += num_item['thLetter']
                elif char == '.':
                    num_str += char

            num_str2 = ''
            temp_str = num_str.split(".")
            int_str = temp_str[0]
            count = 0
            for i in range(len(int_str) - 1, -1, -1):
                element = int_str[i]
                if count < 3:
                    count += 1
                else:
                    count = 1
                    if include_comma:
                        num_str2 = ',' + num_str2
                num_str2 = element + num_str2
            if len(temp_str) > 1 and temp_str[1]:
                num_str2 += '.' + temp_str[1]

            result = num_str2

        return result

    def thai_to_mon(self, thai_number_str):
        result = ''

        if thai_number_str:
            str_chars = list(str(thai_number_str))
            num_str = ''
            for char in str_chars:
                num_item = next((val for val in self.numbers if val['thLetter'] == char), None)
                if num_item:
                    num_str += num_item['letter']
                elif char == '.':
                    num_str += char

            result = num_str

        return result

    def extract_numbers(self, mon_num):
        result = []

        if mon_num:
            temp_str = mon_num.split(".")
            chars_dec = temp_str[1] if len(temp_str) > 1 else ''
            if chars_dec:
                for char in reversed(chars_dec):
                    num_prefix = next((val for val in self.numbers if val['letter'] == char), None)
                    if num_prefix:
                        result.append(num_prefix)
                result.append(self.symbols[0])  # Decimal symbol

            chars = temp_str[0]
            digit = 1
            for char in reversed(chars):
                if digit > 1:
                    num_prefix = next((val for val in self.numbers if val['letter'] == char), None)
                    if num_prefix and num_prefix['number'] > 0:
                        num_suffix = next((val for val in self.numbers if val['digit'] == digit), None)
                        if num_suffix:
                            num = num_suffix.copy()
                            if num_prefix['number'] > 1:
                                num['number'] *= num_prefix['number']
                                num['letter'] = num['letter'].replace('၁', num_prefix['letter'])
                                num['thLetter'] = num['thLetter'].replace('๑', num_prefix['thLetter'])
                                num['spelling'] = num_prefix['spelling'] + num['spelling']
                                num['ipa'] = num_prefix['ipa'] + '-' + num['ipa']
                                num['th'] = num_prefix['th'] + '-' + num['th']
                            result.append(num)
                else:
                    num_item = next((val for val in self.numbers if val['digit'] == digit and val['letter'] == char), None)
                    if num_item:
                        num = num_item.copy()
                        if len(chars) > 1 and num_item['number'] == 0:
                            num = {}
                        else:
                            if num_item['number'] == 5:
                                num['spelling'] = num.get('spelling2', num['spelling'])
                                num['ipa'] = num.get('ipa2', num['ipa'])
                                num['th'] = num.get('th2', num['th'])
                            if num:
                                result.append(num)
                digit += 1

        return result

    def combine_numbers(self, extracted):
        obj = {}
        spelling = ''
        ipa = ''
        th = ''
        for index, val in enumerate(extracted):
            if 'spelling' in val:
                spelling = val['spelling'] + ('' if index == 0 else '-') + spelling
            if 'ipa' in val:
                ipa = val['ipa'] + ('' if index == 0 else '-') + ipa
            if 'th' in val:
                th = val['th'] + ('' if index == 0 else '-') + th
        obj['spelling'] = spelling
        obj['ipa'] = ipa
        obj['th'] = th
        return obj

    def convert_from_mon(self, mon_number_str, include_comma):
        obj = {
            'monNum': '',
            'thaiNum': '',
            'arabicNum': '',
            'spelling': '',
            'ipa': '',
            'th': ''
        }

        obj['monNum'] = mon_number_str
        obj['thaiNum'] = self.mon_to_thai(mon_number_str, include_comma)
        obj['arabicNum'] = self.mon_to_arabic(mon_number_str, include_comma)

        extracted = self.extract_numbers(obj['monNum'])
        obj2 = self.combine_numbers(extracted)

        obj.update(obj2)

        return obj

    def convert_from_arabic(self, arabic_number_str, include_comma):
        obj = {
            'monNum': '',
            'thaiNum': '',
            'arabicNum': '',
            'spelling': '',
            'ipa': '',
            'th': ''
        }

        obj['monNum'] = self.arabic_to_mon(arabic_number_str, include_comma)
        obj['thaiNum'] = self.mon_to_thai(obj['monNum'], include_comma)
        obj['arabicNum'] = arabic_number_str

        extracted = self.extract_numbers(obj['monNum'])
        obj2 = self.combine_numbers(extracted)

        obj.update(obj2)

        return obj

    def convert_from_thai(self, thai_number_str, include_comma):
        obj = {
            'monNum': '',
            'thaiNum': '',
            'arabicNum': '',
            'spelling': '',
            'ipa': '',
            'th': ''
        }

        obj['monNum'] = self.thai_to_mon(thai_number_str, include_comma)
        obj['thaiNum'] = thai_number_str
        obj['arabicNum'] = self.mon_to_arabic(obj['monNum'], include_comma)

        extracted = self.extract_numbers(obj['monNum'])
        obj2 = self.combine_numbers(extracted)

        obj.update(obj2)

        return obj

    def zero_pad(self, num, places):
        if float(num) < 10:
            return str(num).zfill(places)
        return str(num)
