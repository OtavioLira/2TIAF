from nltk.tokenize import word_tokenize
text = "O rato roeu a roupa do rei de roma"
tokens = word_tokenize(text, language="portuguese")
print(tokens)