import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words("portuguese"))

text = "Isso é um exemplo de uso para remoção de stopwords em um texto no idioma portugues..."

words = word_tokenize(text)

filtered_words = [word for word in words if word.lower() not in stopwords]

filtered_text = " ".join(filtered_words)

print("Texto Original")
print(text)
print("\nTexto com stopworlds removidos")
print(filtered_text)