from streamlit_punctuate import text_punctuated
import pytest


def test_punctuated():
    assert text_punctuated("однако на улице прекрасная погода") == "Однако, на улице прекрасная погода."


def test_raises():
    with pytest.raises(Exception) as exc_info:   
        raise Exception("Невозможно определить язык! Попробуйте \
            ввести текст еще раз.")
    # these asserts are identical; you can use either one   
    assert exc_info.value.args[0] == "Невозможно определить язык! Попробуйте \
            ввести текст еще раз."