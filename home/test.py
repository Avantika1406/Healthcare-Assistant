from langdetect import detect
from translate import Translator
import re

def detect_language(text):
    """
    Detect the language of the given text.

    Parameters:
        text (str): The text to detect the language.

    Returns:
        str: The detected language code.
    """
    try:
        language_code = detect(text)
        return language_code
    except Exception as e:
        print(f"Language detection error: {e}")
        return None

def translate_to_english(text, source_language):
    """
    Translate the given text to English.

    Parameters:
        text (str): The text to be translated.
        source_language (str): The language code for the source language.

    Returns:
        str: The translated text in English.
    """
    try:
        translator = Translator(to_lang="en", from_lang=source_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Translation error: {e}")
        return None
 


def translate_to_original_language(text, target_language):

    try:
        translator = Translator(to_lang=target_language, from_lang="en")
        translation = translator.translate(text)
        return translation
    except Exception as e:
        print(f"Translation error: {e}")
        return None
    

import home.ollamaAPI as ollamaAPI
import home.ollama_result_parser as ollama_result_parser
if __name__ == "__main__":
    # Example usage:
    user_input = str(input("MSG:"))
    detected_language = detect_language(user_input)

    if detected_language:
        print(f"Detected Language Code: {detected_language}")

        # Translate the input to English
        english_text = translate_to_english(user_input, detected_language)

        if english_text:
            print(f"Translated to English: {english_text}")

            result  = ollamaAPI.ChatGPTApi.run(english_text)

            # Translate the processed result back to the original language
            final_result = translate_to_original_language(ollama_result_parser.ChatGPTResultParser.parse_result(result), detected_language)
            print(f"Final Result in Original Language: {final_result}")
