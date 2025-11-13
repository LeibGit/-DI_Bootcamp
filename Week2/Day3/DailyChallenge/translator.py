from googletrans import *
import asyncio


async def translate():
    translator_dict = {}

    trans = Translator()

    french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

    for value in french_words:
        val = await trans.translate(value)
        translator_dict[value] = val.text
    print(translator_dict)

asyncio.run(translate())