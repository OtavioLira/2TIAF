import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

#nltk.download('rslp')

stemmer = RSLPStemmer()

text = "Eu estava pensando que poderia ter sido melhor..."

# Tokenizar o texto em paalavras
words = word_tokenize(text, language="portuguese")

stemmed_words = [stemmer.stem(word) for word in words]

stemmed_text = " ".join(stemmed_words)

print("Texto Original")
print(text)
print("\nTexto com stopworlds removidos")
print(stemmed_text)
