import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

text = "O novo livro do autor sera lancado em breve na feira do livro"

words = word_tokenize(text, language="portuguese")

lemmatizer_words = [lemmatizer.lemmatize(word) for word in words]

lemmatizer_text = " ".join(lemmatizer_words)

print("Texto Original")
print(text)
print("\nTexto com stopworlds removidos")
print(lemmatizer_text)
