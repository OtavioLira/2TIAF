import nltk
from nltk.corpus import treebank
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pylab as plt
import seaborn as sns

frase =  """At eight o'clock on Thursday morning
... Arthur didn't feel very good."""

nltk.download('averaged_perceptron_tagger')
nltk.download("punkt")
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('treebank')

tokens = nltk.word_tokenize(frase)
print(tokens)

tag = nltk.pos_tag(tokens)
print(tag[0:6])

entidades = nltk.chunk.ne_chunk(tag)
print(entidades)

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(tag)
tree.draw()

#t = treebank.parsed_sents("Dev\NLTK\frase.mrg")[0]
#t.draw()

# Texto de exemplo
texto = "O cachorro pulou a cerca. O gato correu para longe. O pássaro voou para o céu."

# Tokenização de texto em palavras
palavras = word_tokenize(texto.lower()) # Converte para minúsculas para tratar 'O' para 'o' como iguais

# Cálculo de frequência das palavras
frequencia = FreqDist(palavras)

# Exibição das 10 palavras mais frequentes
print("Palavras mais frequentes: ")
for palavra, freq in frequencia.most_common(10):
    print(f"{palavra}: {freq}")

top_palavras = frequencia.most_common(10)
palavras, freqs = zip(*top_palavras)

sns.set_style("darkgrid")

# Plotando o gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(palavras, freqs, color="skyblue")
plt.title("Top 10 palavras mais frequentes")
plt.xlabel("Palavra")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.show()

tagged_tokens = nltk.pos_tag(tokens, lang='eng')

# Obtém as tags POS de cada token
tags = [tag for _, tag in tagged_tokens]

# Calcula a frequência das tags POS
freq_tags = nltk.FreqDist(tags)

# Obtém as tags POS únicas e suas frequências
unique_tags = freq_tags.keys()
freqs = freq_tags.values()

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(unique_tags, freqs, color='purple')
plt.title('Distribuição das Tags POS')
plt.xlabel('Tag POS')
plt.ylabel('Frequência')
plt.show()