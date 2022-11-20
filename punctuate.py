from sbert_punc_case_ru import SbertPuncCase


model = SbertPuncCase()
print(model.punctuate("sbert punc case расставляет точки запятые и знаки вопроса вам нравится"))

print(model.punctuate("где продаются книги если идёт дождь"))
print(model.punctuate("однако на улице прекрасная погода"))
print(model.punctuate("где вы завтракали"))
