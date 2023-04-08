import streamlit as st
from sbert_punc_case_ru import SbertPuncCase
import string

# Создаём объект - модель для преобразования текста
model = SbertPuncCase()

# Формируем заголовок для браузера
st.title("Восстанавление пунктуации текста")
st.subheader("Применяется после аудиораспознавания, а также при сомнениях после перевода текста.")

# Забираем текст, введённый пользователем в браузере
# ! Была изменена переменная text_to_punctuate на input_text 
# ! для возможности проверки введённого пользователем текста в целях отладки приложения.
input_text = st.text_area("Вставьте сюда текст на русском языке, например - однако на улице прекрасная погода",
                                 value="")

# обработаем текст, на случай, если пользователь ввёл не по правилам -
# преобразуем в нижний регистр и уберём знаки препинания.
# ! Была изменена переменная text_to_punctuate на lowercase_text 
# ! Причины изменения можно посмотреть выше. 
lowercase_text = input_text.lower()
text_to_punctuate = lowercase_text.translate(str.maketrans('', '', string.punctuation))


def text_punctuated(text_to_punctuate):
    """Преобразуем текст, проводя его через модель"""
    return model.punctuate(text_to_punctuate)


# Пишем в браузере преобразованный текст,
st.text_area("Преобразованный текст. Его можно выделить и скопировать.", value=text_punctuated(text_to_punctuate),
             disabled=False)
