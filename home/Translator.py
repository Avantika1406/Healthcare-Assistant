from langdetect import detect
from deep_translator import GoogleTranslator

def translate_text_safe(text, target_lang):
    try:
        src_lang = detect(text)
        if src_lang == target_lang:
            return text
        return GoogleTranslator(
            source=src_lang,
            target=target_lang
        ).translate(text)
    except Exception:
        return text
