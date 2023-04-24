from streamlit_punctuate import text_punctuated, lang_detection


def test_punctuated():
    assert text_punctuated("однако на улице прекрасная погода") == \
        "Однако, на улице прекрасная погода."


def test_lang_detection():
    assert lang_detection("the weather is great in Moscow") == \
        "Язык введенного текста не русский! Попробуйте ввести текст еще раз."
    assert lang_detection("") == \
        "Невозможно определить язык! Попробуйте ввести текст еще раз."
