import spacy
print(spacy.__version__)

# Carregar o modelo para o idoma português
nlp = spacy.load("pt_core_news_sm")

# Texto para ser tokenizado
texto = "O spaCy é uma ótima ferramenta para processamento de linguagem natural"
texto2 = "Bill Gates fundou a microsoft em 1975. Ele nasceu em Seattle."
texto3 = "Eu estava correndo quando vi uma corrida de carros"
texto4 = "João comprou um livro"

# Tokenizar o texto
doc = nlp(texto)

# Exibir tokens
for token in doc:
    print(f"""token: {token.text}
    Forma básica: {token.lemma_}
    Classe gramatical: {token.pos_}
    Tag de detalhes: {token.tag_}""")

# Entidades Nomeadas
doc = nlp(texto2)
for entidade in doc.ents:
    print(f"Entidade: {entidade.text}, Tipo: {entidade.label_}")

# Lemas
doc = nlp(texto3)
for token in doc:
    print(f"Palavra: {token.text}, lemma: {token.lemma_}")

# Exibir as relações de dependências entre palavras
doc = nlp(texto4)

for token in doc:
    print(f"""Palavra: {token.text}
          Dependência: {token.dep_}
          Governante: {token.head.text}""")