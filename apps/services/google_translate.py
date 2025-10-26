import asyncio
from googletrans import Translator

async def translate_text():
     async with Translator() as translator:
         result = await translator.translate('안녕하세요.')
         print(result)  # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
         result = await translator.translate('안녕하세요.', dest='ja')
         print(result)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
         result = await translator.translate('นกพิราบ', src='th', dest='en')
         print(result)  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
         result = await translator.translate('นกพิราบ', src='th', dest='my')
         print(result)  # <Translated src=th dest=en text=dove pronunciation=dove>

async def translate_bulk():
     async with Translator() as translator:
         translations = await translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
         for translation in translations:
             print(translation.origin, ' -> ', translation.text)
             # The quick brown fox  ->  빠른 갈색 여우
             # jumps over  ->  이상 점프
             # the lazy dog  ->  게으른 개


async def translate_tha_to_eng(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='th', dest='en')
        return result.text
    
async def translate_tha_to_mya(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='th', dest='my')
        return result.text
    
async def translate_mya_to_eng(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='my', dest='en')
        return result.text

async def translate_mya_to_tha(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='my', dest='th')
        return result.text

#asyncio.run(translate_bulk())
#asyncio.run(translate_text())