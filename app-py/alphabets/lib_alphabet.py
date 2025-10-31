from alphabets.lib_rule import LibRule
from alphabets.lib_consonant import LibConsonant
from alphabets.lib_vowel import LibVowel
from alphabets.lib_compound_consonant import LibCompoundConsonant
from alphabets.lib_final_consonant import LibFinalConsonant
from alphabets.lib_double_consonant import LibDoubleConsonant
from alphabets.lib_numeral import LibNumeral

# This file defines the Mon language alphabets, including consonants, vowels, numbers, and punctuation.
# It also includes methods to retrieve specific consonants and check their tones.

class LibAlphabet:
    def __init__(self, lib_rule=None, lib_consonant=None, lib_vowel=None, lib_compound_consonant=None, lib_final_consonant=None, lib_double_consonant=None, lib_numeral=None):
        self.lib_rule = lib_rule or LibRule()
        self.lib_consonant = lib_consonant or LibConsonant()
        self.lib_vowel = lib_vowel or LibVowel()
        self.lib_compound_consonant = lib_compound_consonant or LibCompoundConsonant()
        self.lib_final_consonant = lib_final_consonant or LibFinalConsonant()
        self.lib_double_consonant = lib_double_consonant or LibDoubleConsonant()
        self.lib_numeral = lib_numeral or LibNumeral()
        
        self.consonants = self.lib_consonant.get_all()
        self.vowels = self.lib_vowel.get_all()
        self.other_vowels = self.lib_vowel.get_all_other_vowels()
        self.compound_consonants = self.lib_compound_consonant.get_all()
        self.final_consonants = self.lib_final_consonant.get_all_groups()
        self.rules = self.lib_rule.get_all()

    def is_breathy_consonant(self, letter):
        return self.lib_rule.is_breathy_consonant(letter)

    def is_clear_consonant(self, letter):
        return self.lib_rule.is_clear_consonant(letter)

    def get_consonant_by_position(self, row, column):
        return self.lib_consonant.get_by_position(row, column)

    def get_double_example_direct(self):
        return self.lib_double_consonant.get_example_direct()

    def get_double_example_pali_sansakrit(self):
        return self.lib_double_consonant.get_example_pali_sansakrit()

    def craft_word2(self, consonant, compound, vowel, final_consonant):
        print('CRAFT WORD:', 'CON', consonant, 'COM', compound, 'VOW', vowel, 'FIN', final_consonant)
        ipa = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}
        ipa2 = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}
        th = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}
        th2 = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}
        word = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}
        word2 = {'consonant': '', 'compound': '', 'vowel': '', 'final': ''}

        # If no consonant is provided, we use the default consonant
        print('CONSONANT PROVIDED:', consonant)
        current_consonant = self.lib_consonant.get_by_letter(consonant) if consonant else self.lib_consonant.get_by_letter('အ')

        # check if the consonant is breathy or clear
        is_breathy = self.lib_rule.is_breathy_consonant(current_consonant['letter'])
        cl_bt = 'bt' if is_breathy else 'cl'

        # if no vowel is provided, we use the default vowel
        current_vowel = None
        if vowel:
            print('VOWEL PROVIDED:', vowel)
            current_vowel = (self.lib_vowel.get_by_compound(vowel) or 
                           self.lib_vowel.get_by_letter(vowel) or 
                           self.vowels[0])
        else:
            print('NO VOWEL PROVIDED, USING DEFAULT')
            current_vowel = self.vowels[0]

        # check if a certain vowel has to change its form
        blend_vowel_rule = self.lib_rule.find_blend_vowel(current_vowel['compound'], current_consonant['letter'])
        vowel_compound = blend_vowel_rule['replace'] if blend_vowel_rule else current_vowel['compound']

        # Continue with compound consonant processing...
        compound_consonant_data = self.lib_compound_consonant.get_by_compound(compound) if compound else None
        if compound_consonant_data:
            print('COMPOUND CONSONANT PROVIDED:', compound)
            # append the compound consonant to the word
            word['consonant'] = current_consonant['letter']
            word['compound'] = compound_consonant_data['compound']

            word2['consonant'] = current_consonant['letter']
            word2['compound'] = compound_consonant_data['compound']

            # check if the compound consonant has a blend sound with the current consonant according to the rules
            blend_compound = None
            blend_compound = self.lib_rule.find_blend_compound(compound, current_consonant['letter'])

            if blend_compound:
                print('BLEND COMPOUND FOUND:', blend_compound)
                # if the compound consonant is a blend
                if blend_compound.get('isReversed', False):
                    # swap consonants when reversed (e.g., blends with 'ဟ')
                    a = current_consonant
                    b = compound_consonant_data
                    current_consonant = b
                    compound_consonant_data = a
                    # also change the vowel IPA from BT to CL regardless
                    is_breathy = False

                    # IPA and Thai phonetics for blended compound
                    ipa['consonant'] = current_consonant.get('compoundIPA', '')
                    ipa['compound'] = compound_consonant_data.get('compoundIPA', '')
                    # combine consonant+compound in th.consonant so vowel composition works correctly
                    th['consonant'] = (current_consonant.get('compoundTH', '') or '') + (compound_consonant_data.get('compoundTH', '') or '')
                    th['compound'] = ''

                    ipa2['consonant'] = current_consonant.get('compoundIPA', '')
                    ipa2['compound'] = compound_consonant_data.get('compoundIPA', '')
                    th2['consonant'] = (current_consonant.get('compoundTH', '') or '') + (compound_consonant_data.get('compoundTH', '') or '')
                    th2['compound'] = ''
            else:
                # not a true blend: treat as consonant + compound
                ipa['consonant'] = current_consonant.get('ipa', '')
                ipa['compound'] = compound_consonant_data.get('compoundIPA', '')
                th['consonant'] = current_consonant.get('th', '')
                th['compound'] = compound_consonant_data.get('compoundTH', '')
                ipa2['consonant'] = current_consonant.get('ipa', '')
                ipa2['compound'] = compound_consonant_data.get('compoundIPA', '')
                th2['consonant'] = current_consonant.get('th', '')
                th2['compound'] = compound_consonant_data.get('compoundTH', '')
        else:
            print('NO COMPOUND CONSONANT PROVIDED')
            # no compound consonant provided; use current consonant defaults
            word['consonant'] = current_consonant.get('letter', '') if current_consonant else ''
            word2['consonant'] = current_consonant.get('letter', '') if current_consonant else ''

            ipa['consonant'] = current_consonant.get('compoundIPA', '') if current_consonant else ''
            th['consonant'] = current_consonant.get('compoundTH', 'อ') if current_consonant else 'อ'

            ipa2['consonant'] = current_consonant.get('compoundIPA', '') if current_consonant else ''
            th2['consonant'] = current_consonant.get('compoundTH', 'အ') if current_consonant else 'အ'
        
        final_consonant_data = self.lib_final_consonant.get_by_letter(final_consonant)
        final_consonant_group = self.lib_final_consonant.get_group_by_letter(final_consonant)
        if final_consonant_data and final_consonant_group:
            print('FINAL CONSONANT PROVIDED:', final_consonant)
            # try to analyse with vowels according to rules of finalWith and also with blendFinals.
            allowed_vowel = next((vowel for vowel in final_consonant_group['finalWith'] 
                                  if current_vowel['compound'] == vowel['vowel'] or 
                                  ('compound2' in current_vowel and current_vowel['compound2'] == vowel['vowel'])), None)

            # if final consonant is compatible with the current vowel
            if allowed_vowel:
                # check if there's any blend rules for final consonant and vowel
                blend_final = self.lib_rule.find_blend_final(final_consonant_data['final'])

                if blend_final:
                    # if there's a blend rule, replace the vowel with the blend rule
                    replace_vowel = next((v for v in blend_final['vowels'] if v['vowel'] == vowel_compound), None)
                    if replace_vowel:
                        # if replace vowel found, use the replaceVowel instead of final consonant and vowel in word2
                        word2['vowel'] = replace_vowel['replace']

                # anyway, we can append the final consonant and vowel to the word
                word['vowel'] = vowel_compound
                word['final'] = final_consonant_data['final']

                # append the IPA-TH for final consonant and vowel
                ipa['vowel'] = allowed_vowel['ipaBT'] if is_breathy else allowed_vowel['ipaCL']
                ipa['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalIPA']
                th['vowel'] = allowed_vowel['thBT'] if is_breathy else allowed_vowel['thCL']
                th['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalTH']

                if is_breathy and 'ipaBT2' in allowed_vowel:
                    ipa2['vowel'] = allowed_vowel['ipaBT2']
                    ipa2['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalIPA']
                    th2['vowel'] = allowed_vowel['thBT2']
                    th2['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalTH']
                if not is_breathy and 'ipaCL2' in allowed_vowel:
                    ipa2['vowel'] = allowed_vowel['ipaCL2']
                    ipa2['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalIPA']
                    th2['vowel'] = allowed_vowel['thCL2']
                    th2['final'] = '' if final_consonant_group['isSilent'] else final_consonant_data['finalTH']
            else:
                # reject final consonant and skip to the next layer which is vowel
                word['vowel'] = vowel_compound
                ipa['vowel'] = allowed_vowel['ipaBT'] if is_breathy else allowed_vowel['ipaCL']
                th['vowel'] = allowed_vowel['thBT'] if is_breathy else allowed_vowel['thCL']

                if is_breathy and 'ipaBT2' in current_vowel:
                    ipa2['vowel'] = current_vowel['ipaBT2']
                    th2['vowel'] = current_vowel['thBT2']
                if not is_breathy and 'ipaCL2' in current_vowel:
                    ipa2['vowel'] = current_vowel['ipaCL2']
                    th2['vowel'] = current_vowel['thCL2']
        else:
            print('NO FINAL CONSONANT PROVIDED OR NOT COMPATIBLE:', final_consonant)
            # if no final consonant data, we then skip to the next layer which is vowel
            word['vowel'] = vowel_compound
            ipa['vowel'] = current_vowel['ipaBT'] if is_breathy else current_vowel['ipaCL']
            th['vowel'] = current_vowel['thBT'] if is_breathy else current_vowel['thCL']

            if is_breathy and 'ipaBT2' in current_vowel:
                ipa2['vowel'] = current_vowel['ipaBT2']
                th2['vowel'] = current_vowel['thBT2']
            if not is_breathy and 'ipaCL2' in current_vowel:
                ipa2['vowel'] = current_vowel['ipaCL2']
                th2['vowel'] = current_vowel['thCL2']

        #print ipa
        print('IPA:', ipa)

        # Convert JS blend TH checks to Python: if vowel and final present, apply blend replacement
        if th.get('vowel') and th.get('final'):
            blend_th = self.lib_rule.find_blend_th(th.get('vowel'))
            if blend_th and blend_th.get('replace') is not None:
                th['vowel'] = blend_th.get('replace')

        if th2.get('vowel') and th2.get('final'):
            blend_th = self.lib_rule.find_blend_th(th2.get('vowel'))
            if blend_th and blend_th.get('replace') is not None:
                th2['vowel'] = blend_th.get('replace')

        # store processed information
        result_word = (word.get('consonant', '') +
                       word.get('compound', '') +
                       word.get('vowel', '') +
                       word.get('final', ''))

        result_word2 = ''
        if word2.get('vowel'):
            result_word2 = (word2.get('consonant', '') +
                            word2.get('compound', '') +
                            word2.get('vowel', '') +
                            word2.get('final', ''))

        result_ipa = (ipa.get('consonant', '') +
                      ipa.get('compound', '') +
                      ipa.get('vowel', '') +
                      ipa.get('final', ''))

        result_ipa2 = ''
        if ipa2.get('vowel'):
            result_ipa2 = (ipa2.get('consonant', '') +
                           ipa2.get('compound', '') +
                           ipa2.get('vowel', '') +
                           ipa2.get('final', ''))

        # IPA composition: replace 'ʔ' in vowel with compound or consonant as needed
        vowel_ipa = ipa.get('vowel', '')
        if ipa.get('compound'):
            result_ipa = (ipa.get('consonant', '') +
                         vowel_ipa.replace('ʔ', ipa.get('compound', '')))
        else:
            result_ipa = (vowel_ipa.replace('ʔ', ipa.get('consonant', '')))

        # For result_ipa2 follow the original JS logic: if ipa2.vowel exists then build, else empty
        if ipa2.get('vowel'):
            if ipa2.get('compound'):
                result_ipa2 = (ipa2.get('consonant', '') +
                              ipa2.get('vowel', '').replace('ʔ', ipa2.get('compound', '')))
            else:
                result_ipa2 = (ipa2.get('vowel', '').replace('ʔ', ipa2.get('consonant', '')))
        else:
            result_ipa2 = ''

        # TH composition: replace '-' in vowel with compound or consonant as needed
        vowel_th = th.get('vowel', '')
        if th.get('compound'):
            result_th = (th.get('consonant', '') +
                         vowel_th.replace('-', th.get('compound', '')))
        else:
            result_th = (vowel_th.replace('-', th.get('consonant', '')))

        # For result_th2 follow the original JS logic: if th2.vowel exists then build, else empty
        if th2.get('vowel'):
            if th2.get('compound'):
                # note: original JS used th.consonant here, preserve that behavior
                result_th2 = (th2.get('consonant', '') +
                              th2.get('vowel', '').replace('-', th2.get('compound', '')))
            else:
                result_th2 = (th2.get('vowel', '').replace('-', th2.get('consonant', '')))
        else:
            result_th2 = ''

        # Return the result dictionary
        return {
            'word': result_word,
            'word2': result_word2,
            'cl_bt': cl_bt,
            'ipa': result_ipa,
            'ipa2': result_ipa2,
            'th': result_th,
            'th2': result_th2
        }

    def analyse_text(self, text):
        # Convert string to list of characters, filter out empty spaces
        chars = [c for c in (text or '') if c]
        
        memories = []
        current_word = ''
        word_finished = False
        index = 0
        length = len(chars)
        print(f"CHARS: {chars} | LENGTH: {length}")
        
        while index < length:
            i_prev = index - 1
            i_next = index + 1
            
            char_prev = chars[i_prev] if i_prev >= 0 else None
            char_current = chars[index]
            char_next = chars[i_next] if i_next < length else None
            
            # Classification checks
            is_consonant = self.lib_consonant.is_consonant(char_current)
            is_stand_alone_vowel = self.lib_vowel.is_stand_alone_vowel(char_current)
            is_compound_vowel = self.lib_vowel.is_compound_vowel(char_current)
            is_compound_consonant = self.lib_compound_consonant.is_compound_consonant(char_current)
            is_double_symbol = self.lib_double_consonant.is_double_symbol(char_current)
            is_final_symbol = self.lib_final_consonant.is_final_symbol(char_current)
            is_final2_symbol = self.lib_final_consonant.is_final2_symbol(char_current)
            double_consonant = self.lib_double_consonant.get_by_doubled(char_current)
            is_number_char = self.lib_numeral.is_number_char(char_current)

            if is_consonant:
                print('is_consonant', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # A. check if this char is registered as a consonant
                print('INDEX:', i_prev, 'LENGTH:', i_next)
                if i_prev >= 0 and i_next < length:
                    # A-2 before register this consonant to the currentWord 
                    # we must try to analyse if this consonant is the last one in the currentWord
                    # if that's the case, we have to separate it into a new word. 
                    # If not, we'll let it continue
                    # ----a. the prev char is a consonant (or vowel) and the next char is a vowel
                    # ----b. the next char must not be the final symbol 
                    # ----c. if the next char is a double symbol then further check if 
                    # ------c.1 it's not the PaliSansakrit double consonant

                    prev_is_consonant = self.lib_consonant.is_consonant(char_prev)
                    prev_is_vowel = self.lib_vowel.is_compound_vowel(char_prev)
                    next_is_consonant = self.lib_consonant.is_consonant(char_next)
                    next_is_vowel = self.lib_vowel.is_compound_vowel(char_next)
                    next_is_compound = self.lib_compound_consonant.is_compound_consonant(char_next)
                    next_is_final_symbol = self.lib_final_consonant.is_final_symbol(char_next)
                    next_is_double_symbol = self.lib_double_consonant.is_double_symbol(char_next)
                    next_char_next2 = chars[i_next + 1] if i_next + 1 < length else ''
                    next2_is_pali_sansakrit = self.lib_double_consonant.is_double_consonant2(char_current, next_char_next2)

                    if (prev_is_consonant or prev_is_vowel) and (next_is_consonant or next_is_vowel):
                        # there's some double consonants that disguise as a single consonant
                        # we have to check first before moving on
                        current_double_consonant = self.lib_double_consonant.get_by_doubled(char_current)
                        if current_double_consonant:
                            current_word += current_double_consonant['converts'][0]

                        # completed
                        print('CLASSIFIED-A', char_current)
                        if current_word:
                            memories.append(current_word)
                        current_word = '' + char_current
                    elif next_is_double_symbol and not next2_is_pali_sansakrit:
                        # in case we find the Direct double consonant
                        print('CLASSIFIED-B', char_current)
                        if current_word:
                            memories.append(current_word)
                        current_word = '' + char_current
                    elif not next_is_final_symbol and not next_is_double_symbol and not next2_is_pali_sansakrit and not next_is_compound:
                        # maybe the next char is vowel or consonant
                        print('CLASSIFIED-C', char_current)
                        if current_word:
                            memories.append(current_word)
                        current_word = '' + char_current
                    elif next_is_compound:
                        # maybe the next is a compound consonant 
                        # but do check first if it goes according to the rule

                        # there's some PaliSansakrit double consonants that disguise as a compound consonant
                        current_double_consonant2 = self.lib_double_consonant.get_by_pali_sansakrit2(char_current, char_next)
                        if current_double_consonant2:
                            print('CLASSIFIED-D2', char_current)
                            current_word += current_double_consonant2['converts'][0]
                            char_next = current_double_consonant2['converts'][1]

                            if current_word:
                                memories.append(current_word)

                            current_word = '' + char_next
                            word_finished = True
                            index += 1
                        else:
                            print('CLASSIFIED-D1', char_current)
                            if current_word:
                                memories.append(current_word)
                            current_word = '' + char_current
                    else:
                        print('UNCLASSIFIED')
                        current_word += char_current
                else:
                    # if it's the last
                    # finish a word
                    if i_next >= length:
                        print('CLASSIFIED-E', char_current)

                        # there's some double consonants that disguise as a single consonant
                        current_double_consonant = self.lib_double_consonant.get_by_doubled(char_current)
                        if current_double_consonant:
                            current_word += current_double_consonant['converts'][0]

                        if current_word:
                            memories.append(current_word)
                        current_word = '' + char_current
                        word_finished = True
                    else:
                        # this char is the first (or the last) char in a text
                        current_word += char_current
            elif is_stand_alone_vowel:
                print('is_stand_alone_vowel', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # B. check if this char is registered as a stand alone vowel
                # immediately register the currentWord into memories
                # then start a new
                if current_word:
                    memories.append(current_word)
                current_word = '' + char_current
            elif is_compound_vowel:
                print('is_compound_vowel', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # C. add it to the currentWord
                current_word += char_current
                # if it's the last
                # finish a word
                if i_next >= length:
                    word_finished = True
            elif is_compound_consonant:
                print('is_compound_consonant', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # D. add it to the currentWord
                current_word += char_current

                # if it's the last
                # finish a word
                if i_next >= length:
                    word_finished = True
            elif is_double_symbol:
                print('is_double_symbol', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # E. let's try to check if it's 
                # -----a. Compound consonant
                # -----b. PaliSansakrit double consonant
                # -----c. Direct double consonant
                a_is_compound_consonant = self.lib_compound_consonant.is_compound_consonant2(char_prev, char_next)
                a_is_pali_sansakrit = self.lib_double_consonant.is_double_consonant2(char_prev, char_next)

                if a_is_pali_sansakrit:
                    print('CLASSIFIED-F', char_current, char_next)
                    # it's 2 words according to Pali-Sansakrit rule
                    current_word += self.lib_final_consonant.final_symbol
                    word_finished = True
                elif a_is_compound_consonant:
                    # move on to the next +2 index
                    current_word += char_current + char_next
                    index += 1
                else:
                    # it's 2 words according to Direct rule
                    word_finished = True

            elif is_final_symbol:
                print('is_final_symbol', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # F. the prev consonant is the final consonant, thus the current word is completed. 
                current_word += char_current

                # however there might be some exception if the next char is some kind of final2 symbol
                next_blend_final = char_current + char_next
                prev_blend_final = char_current + char_prev
                next_is_final2_symbol = self.lib_final_consonant.is_final2_symbol(next_blend_final)
                prev_is_final2_symbol = self.lib_final_consonant.is_final2_symbol(prev_blend_final)
                prev_is_compound_symbol = self.lib_compound_consonant.is_compound_consonant(char_prev)

                if not next_is_final2_symbol and not prev_is_final2_symbol:
                    word_finished = True
                if prev_is_compound_symbol:
                    word_finished = True

                # v1.7.2 check if there's a double final consonant, if true that means it's a repetition word (same as "ๆ" in Thai)
                next_char_next2 = chars[i_next + 1] if i_next + 1 < length else ''
                current_final = char_prev + char_current
                next_same_final = char_next + next_char_next2
                if current_final == next_same_final:
                    # skip 2 step
                    index += 2
                    # add 1 word
                    if current_word:
                        memories.append(current_word)
                    # then let the same word get added later
                    word_finished = True

            elif is_final2_symbol:
                print('is_final2_symbol', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # G. the current consonant is the final consonant that blends itself with some vowel
                current_word += char_current

            elif double_consonant:
                print('is_double_consonant', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # H. the current consonant is a special double consonant
                # this is a special case, we have to check if it's a PaliSansakrit double consonant
                print('DOUBLE-CONSONANT', char_current)
                current_word += double_consonant['converts'][0]
                if current_word:
                    memories.append(current_word)

                current_word = '' + double_consonant['converts'][1]
            elif is_number_char:
                print('is_number_char', 'CURRENT:', char_current, 'PREV:', char_prev, 'NEXT:', char_next)
                # v1.7.4 numeral recognition
                is_next_char_number = self.lib_numeral.is_number_char(char_next)
                is_next_char_num_symbol = self.lib_numeral.is_symbol(char_next)
                is_prev_char_number = self.lib_numeral.is_number_char(char_prev)
                is_prev_char_num_symbol = self.lib_numeral.is_symbol(char_prev)

                # check if user write number close to the previous word, then cut the previous word out first
                if not is_prev_char_number and not is_prev_char_num_symbol:
                    if current_word:
                        memories.append(current_word)
                    # reset currentWord
                    current_word = ''
                else:
                    current_word += char_current

                # if the next char is either . or ,
                if is_next_char_num_symbol:
                    current_word += char_next
                    index += 1

                # next char is neither number or num symbol then end this as a word
                if not is_next_char_number and not is_next_char_num_symbol:
                    word_finished = True
            else:
                # maybe it was some spacing or punctuations, or untrained characters
                word_finished = True
                print('INVALID CHAR:', char_current)

            # Handle word completion
            if word_finished or index >= length - 1:
                print('WORD FINISHED:', current_word)
                if current_word:
                    memories.append(current_word)
                current_word = ''
                word_finished = False
            
            index += 1

        # Process results
        analysed = []
        ipa = ''
        th = ''
        ipas = []
        ths = []
        allIpa = []
        allTh = []
        
        for i in range(len(memories)):
            word = memories[i]
            craft = self.analyse_single_word(word)
            # re-assign value in case there's a better option from analysed word
            memories[i] = craft['word']
            analysed.append(craft)

            n_ipa = craft['crafted']['ipa']
            n_th = craft['crafted']['th']
            n_ipa2 = craft['crafted'].get('ipa2', None)
            n_th2 = craft['crafted'].get('th2', None)

            # exception if the vowel is a stand-alone vowel, always use the default ipa
            if self.lib_vowel.is_stand_alone_vowel(craft['structure']['vowel']):
                n_ipa = craft['crafted']['ipa']
                n_th = craft['crafted']['th']
                n_ipa2 = None
                n_th2 = None

            #ipa += n_ipa + ('-' if i < len(memories) - 1 else '')
            #th += n_th + ('-' if i < len(memories) - 1 else '')
            ipa += n_ipa + ('' if i < len(memories) - 1 else '')
            th += n_th + ('' if i < len(memories) - 1 else '')

            # collect all possible ipa & th
            tempIpa = []
            tempTh = []
            if n_ipa:
                tempIpa.append(n_ipa)
            if n_ipa2:
                tempIpa.append(n_ipa2)
            if n_th:
                tempTh.append(n_th)
            if n_th2:
                tempTh.append(n_th2)
            ipas.append(tempIpa)
            ths.append(tempTh)

        # generate all possible pronunciations
        allIpa = self.generate_cartesian_products(ipas)
        allTh = self.generate_cartesian_products(ths)

        return {
            'text': text,
            'syllables': memories,
            'analysed': analysed,
            'ipa': ipa,
            'th': th,
            'ipas': ipas,
            'ths': ths,
            'ipas': allIpa,
            'ths': allTh,
            'deconstructs': chars
        }

    def analyse_single_word(self, word):
        # convert string to list of characters, filter out empty spaces
        chars = [c for c in (word or '')]
        chars = [c for c in chars if c]

        # try numeral lookup (support either snake_case or camelCase impls)
        num = None
        if hasattr(self.lib_numeral, 'get_number'):
            num = self.lib_numeral.get_number(word)
        elif hasattr(self.lib_numeral, 'getNumber'):
            num = self.lib_numeral.getNumber(word)

        result = None
        word_structure = {
            'consonant': '',
            'compound': '',
            'vowel': '',
            'final': '',
            'num': ''
        }

        if num:
            result = num
            word_structure['num'] = result.get('monNum') if isinstance(result, dict) else getattr(result, 'monNum', None)
            return {
                'word': word_structure['num'],
                'structure': word_structure,
                'crafted': result
            }
        else:
            index = 0
            length = len(chars)
            while index < length:
                i_prev = index - 1
                i_next = index + 1

                char_prev = chars[i_prev] if i_prev >= 0 else None
                char_current = chars[index]
                char_next = chars[i_next] if i_next < length else None

                consonant = self.lib_consonant.get_by_letter(char_current)
                compound = self.lib_compound_consonant.get_by_compound(char_current)
                vowel = self.lib_vowel.get_by_compound(char_current)
                stand_alone_vowel = self.lib_vowel.get_by_letter(char_current)
                final_consonant = self.lib_final_consonant.get_by_letter(char_current)
                final_symbol = self.lib_final_consonant.is_final_symbol(char_current)
                final2_symbol = self.lib_final_consonant.is_final2_symbol(char_current)

                if consonant:
                    if i_prev >= 0 and i_next < length:
                        next_is_final_symbol = self.lib_final_consonant.is_final_symbol(char_next)
                        prev_is_double_symbol = self.lib_double_consonant.is_double_symbol(char_prev)
                        if prev_is_double_symbol:
                            # it's the compound consonant
                            if compound:
                                word_structure['compound'] = compound.get('letter') if isinstance(compound, dict) else getattr(compound, 'letter', '')
                        elif next_is_final_symbol:
                            # it's the final consonant (combined char_current + char_next)
                            word_structure['final'] = (char_current or '') + (char_next or '')
                            index += 1
                    else:
                        if index == 0:
                            # first char means it's really a consonant
                            word_structure['consonant'] = consonant.get('letter') if isinstance(consonant, dict) else getattr(consonant, 'letter', '')
                        # if it's the last char, ignore (incomplete word)
                elif compound:
                    # some final consonant can disguise itself as a compound symbol
                    next_blend_final = (char_current or '') + (char_next or '')
                    prev_blend_final = (char_current or '') + (char_prev or '')
                    next_is_final2_symbol = self.lib_final_consonant.is_final2_symbol(next_blend_final)
                    prev_is_final2_symbol = self.lib_final_consonant.is_final2_symbol(prev_blend_final)

                    next_blend_final2 = (char_next or '') + (char_current or '')
                    prev_blend_final2 = (char_prev or '') + (char_current or '')
                    next_is_final2_symbol2 = self.lib_final_consonant.is_final2_symbol(next_blend_final2)
                    prev_is_final2_symbol2 = self.lib_final_consonant.is_final2_symbol(prev_blend_final2)

                    if not (next_is_final2_symbol or prev_is_final2_symbol or next_is_final2_symbol2 or prev_is_final2_symbol2):
                        word_structure['compound'] = compound.get('compound') if isinstance(compound, dict) else getattr(compound, 'compound', '')
                    else:
                        word_structure['final'] = compound.get('letter') if isinstance(compound, dict) else getattr(compound, 'letter', '')
                elif stand_alone_vowel:
                    word_structure['vowel'] = stand_alone_vowel.get('letter') if isinstance(stand_alone_vowel, dict) else getattr(stand_alone_vowel, 'letter', '')
                    # assign the next vowel into vowel and skip the next index if present
                    next_vowel = self.lib_vowel.get_by_compound(char_next)
                    if next_vowel:
                        word_structure['vowel'] += next_vowel.get('compound') if isinstance(next_vowel, dict) else getattr(next_vowel, 'compound', '')
                        index += 1
                elif vowel:
                    # if there's no next char and the current vowel is actually a final consonant in disguise, take final instead
                    if char_next is None and final_consonant:
                        word_structure['final'] = final_consonant.get('final') if isinstance(final_consonant, dict) else getattr(final_consonant, 'final', '')
                    else:
                        # multiple sub-vowels combined into one vowel
                        word_structure['vowel'] += vowel.get('compound') if isinstance(vowel, dict) else getattr(vowel, 'compound', '')
                elif final_symbol:
                    # some final consonants are blended that only show a symbol
                    prev_vowel = self.lib_vowel.get_by_compound(char_prev)
                    if prev_vowel:
                        word_structure['final'] = final_consonant.get('final') if final_consonant and isinstance(final_consonant, dict) else getattr(final_consonant, 'final', '') if final_consonant else ''
                elif final2_symbol:
                    # add it into vowel
                    word_structure['vowel'] += char_current
                else:
                    # invalid / unhandled char - ignore
                    pass

                index += 1

            result = self.craft_word2(
                word_structure.get('consonant', ''),
                word_structure.get('compound', ''),
                word_structure.get('vowel', ''),
                word_structure.get('final', '')
            )

            return {
                'word': word,
                'structure': word_structure,
                'crafted': result
            }

    # Utility function to generate Cartesian products
    def generate_cartesian_products(self, arrays):
        result = []

        def helper(current, depth):
            if depth == len(arrays):
                result.append(current)
                return

            for char in arrays[depth]:
                #new_current = current + ('-' if current else '') + char
                new_current = current + ("" if current else '') + char
                helper(new_current, depth + 1)

        helper('', 0)
        return result
