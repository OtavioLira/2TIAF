import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string
from rich import print
import matplotlib.pyplot as plt

# Baixar recursos adicionais do NLTK
nltk.download("punkt")
nltk.download("stopworlds")

# Texto de exemplo
texto = """
O cachorro correu pelo corredor. O gato dormiu na poltrona. O cachorro latiu para o gato.
"""

# Tokenização
tokens = word_tokenize(texto.lower(), language="portuguese") # Convertendo para minúsculo

# Remoção de pontuação e stopworlds
pontuacao = set(string.punctuation)
stop_worlds = set(stopwords.words("portuguese"))
tokens_filtrados = [word for word in tokens if word not in pontuacao and word not in stop_worlds]

# Contagem com frequencia
frequencia = Counter(tokens_filtrados)

# Exibição dos resultados
print("Frequência das palavras")
for palavra, freq in frequencia.items():
    print(f"{palavra}: {freq}")

# Plotagem do gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(frequencia.keys(), frequencia.values())
plt.xticks(rotation=45)
plt.xlabel('Palavra')
plt.ylabel('Frequência')
plt.title('Frequência das Palavras no Texto')
plt.show()

# plotagem do grafico de pizza
plt.figure(figsize=(8, 8))
plt.pie(frequencia.values(), labels=frequencia.keys(), autopct='%1.1fNX')
plt.title('Distribuição das Palavras no Texto')
plt.show()