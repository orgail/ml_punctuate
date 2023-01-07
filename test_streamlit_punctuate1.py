from streamlit_punctuate import text_punctuated

def test_punctuated():
    assert text_punctuated("однако на улице прекрасная погода") == "Однако, на улице прекрасная погода."