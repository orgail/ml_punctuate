import streamlit as st
from sbert_punc_case_ru import SbertPuncCase
import string

# Создаём объект - модель для преобразования текста
model = SbertPuncCase()

# Формируем заголовок для браузера
st.title("Восстанавление пунктуации текста")
st.subheader("Применяется после аудиораспознавания, а также при сомнениях после перевода текста.")

# Забираем текст, введённый пользователем в браузере
text_to_punctuate = st.text_area("Вставьте сюда текст на русском языке, например - однако на улице прекрасная погода", value="")

# обработаем текст, на случай, если пользователь ввёл не по правилам -
# преобразуем в нижний регистр и уберём знаки препинания.
text_to_punctuate = text_to_punctuate.lower()
text_to_punctuate = text_to_punctuate.translate(str.maketrans('', '', string.punctuation))

def text_punctuated(text_to_punctuate):
    """Преобразуем текст, проводя его через модель"""
    return model.punctuate(text_to_punctuate)

# Пишем в браузере преобразованный текст, 
st.text_area("Преобразованный текст. Его можно выделить и скопировать.", value=text_punctuated(text_to_punctuate), disabled=False)
