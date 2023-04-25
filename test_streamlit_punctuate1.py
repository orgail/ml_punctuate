import pytest
from streamlit_punctuate import check_input
from langdetect.lang_detect_exception import LangDetectException
from streamlit_punctuate import text_punctuated


def test_input_ru():
    assert check_input("однако на улице прекрасная погода") == "ru"


def test_input_not_ru():
    assert check_input("This text is in English.") != "ru"


def test_input_symbol():
    with pytest.raises(LangDetectException):
        check_input("#%0)#_)")


def test_punctuated():
    assert text_punctuated("однако на улице прекрасная погода") \
        == "Однако, на улице прекрасная погода."
