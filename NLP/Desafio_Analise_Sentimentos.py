import spacy
from spacytextblob import SpacyTextBlob

print(spacy.__version__)

# Carregar o modelo para o idoma português
nlp = spacy.load('pt_core_news_sm')
nlp.add_pipe("spacytextblob")

# Reviews para serem tokenizado

# 7/10
review1 = """Muitos Titãs lutando. É por isso que vamos para algo assim, certo?
G X K é quase o mesmo em termos de entretenimento que G vs K, embora eu dê uma ligeira vantagem à entrada mais recente por alguns motivos. Por um lado, há um pouco menos de bobagem. Há um alívio cômico, é claro, mas não está fora do lugar ou bobo. Os retrocessos dos anos 80 com músicas, sintetizadores e vibrações foram ótimos. E, por último, os Titãs voltaram a ser os bandidos em vez de humanos. Sempre acho chato quando você assiste a um filme sobre lutas de monstros, mas tem que desvendar uma história de vilões humanos e suas ideologias idiotas.
Uma observação lateral: é hilário que esses Titãs pareçam realmente gostar de ter suas lutas reais nas maiores cidades do planeta ou enquanto destroem algumas das estruturas mais reverenciadas do mundo. Sério, pessoal, vocês não poderiam ter caído no meio do Saara? Mais destruição é igual a mais entretenimento, suponho. Além disso, Godzilla assassina casualmente centenas, senão milhares, apenas andando do ponto A ao ponto B. Estou divagando. Vai rosa Zilla!"""

# 6/10
review2 = """Monstro = viva Humanos = lixo
Outra parcela do Monster-Verse da coleção me deu outro motivo para visitar meu cinema. Felizmente não fiquei desapontado, consegui tudo o que esperava que pudesse ser convocado pelas duas equações acima.
Sobre os humanos: Se você quiser assistir ao filme em casa, não perca tempo com a subtrama dos humanos. É completamente inútil. Os diálogos não são engraçados nem inteligentes. Eles servem uma exposição pobre que é dolorosamente cansativa de assistir. Você vê os monstros lutando e esses “personagens” vão explicando no meio: ah, ele está protegendo! - Qual é, quem escreveu isso? Na minha opinião, se a Legendary Studios quiser incluir humanos, eles deveriam pelo menos tentar torná-los um pouco interessantes ou apenas removê-los completamente. Nenhum deles está fazendo nada necessário e, além disso, o que quer que estejam fazendo não faz sentido. Por que diabos eles estão na Terra Oca sem proteção? Um cara está apenas com uma camisa havaiana. A quantidade de monstros perigosos não é alarmante, eu acho... Paper Boy está filmando tudo, mas o britânico de camisa havaiana diz algo como: É melhor manter isso em segredo, essa civilização antiga não deveria ser exposta aos nossos mundo. A garota de Godzilla vs. Kong (ela é daquele mundo e tem poderes estranhos de X-Men (?)) está entre as pessoas modernas, então o mundo já conhece o mundo subterrâneo. O que ele quer esconder? Há mais dessa estupidez.
Sobre os monstros: Kong é o líder. Sua jornada é simples, ele se sente solitário, quer ter uma família como ela. Pelos trailers, você sabe, há mais macacos gigantes, então estou feliz em vê-los porque sou o Team Kong :) Eu gostaria de apreciar os "diálogos" entre Kong e esse amiguinho ruivo. Eles não usam palavras como nós, mas acredite, esses dois são mais interessantes que os humanos. Você vai gostar.
Godzilla e o resto são apenas monstros. Infelizmente Godzilla não é intimidador neste filme, seu único objetivo é ganhar o nível rosa da energia nuclear e então usá-lo para lutar contra o macaco mau. No entanto, as cenas de luta são fantásticas - é por isso que estamos a ver este tipo de filmes, por isso, se é fã de monstros gigantes, recomendo Godzilla x Kong: O Novo Império... e não espere ver aumento do "novo império" neste filme. É um título meio estranho gerado pelo ChatGPT."""

# 3/10
review3 = """Quando questionado sobre qual é o seu plano, um personagem de Godzilla x Kong: The New Empire diz ‘jogue tudo na parede e veja o que gruda’. O diretor Adam Wingard adotou essa abordagem ao fazer este filme, mas nesta ocasião muito pouco do que está sendo jogado aleatoriamente realmente pega. Os confrontos entre as criaturas do filme são barulhentos, frenéticos e razoavelmente divertidos, mas o enredo é uma merda desleixada de proporções titânicas - uma bagunça fedorenta, artificial e exagerada trazida à vida em um turbilhão de CGI não muito convincente.
O roteiro é absolutamente terrível, e a maior parte do filme me fez coçar a cabeça em confusão ou rir de seu absurdo. Kong sendo equipado com um punho de metal é uma ideia inegavelmente legal, mas o fato de os protagonistas terem tal dispositivo em mãos em Hollow Earth é simplesmente uma loucura (especialmente um com soro anti-congelamento embutido!). Um veterinário que sabe extrair um dente de Kong também sabe pilotar uma nave flutuante da Terra Oca - claramente um homem de muitos talentos. Só Deus sabe o que a tribo Iwi estava fazendo com suas pirâmides brilhantes. Qual foi o problema com aquela ponta brilhante que aquele macaco desagradável usou para controlar o lagarto de gelo? E por que todos de repente começaram a flutuar na Terra Oca? (pode ter havido explicações para alguns destes pontos, mas eles se perderam em todo o caos).
Depois de Godzilla Minus One, sugiro deixar todos os filmes futuros com o grande lagarto para os japoneses.
3,5/10, arredondado para 3 para o olhar perpetuamente ansioso de Kaylee Hottle – a garota não tem nenhuma outra expressão?"""

# 7/10
review4 = """Você recebe o que pagou. Muitos titãs CGI, indo cena por cena, culminando em uma cena de luta final boffo. Eu li alguns artigos online afirmando "há muito CGI.." O filme é centrado em um gorila de quinze metros, um lagarto de dezoito metros, e eles estão lutando contra outros titãs enormes em um mundo que não existe. Ótimos efeitos especiais, ótima ação e um bom ritmo.
História? Não se engane. A história é tão fina quanto a metade de um fio de cabelo. Você veio para a luta dos animais fictícios. Não é suficiente Godzilla. Isso foi uma pena. Vá ver isso se você é fã de filmes idiotas e pipoca. Não espere Otelo."""

# Tokenizar os textos
reviews = [review1, review2, review3, review4]
for review in reviews:
    doc = nlp(review)
    if doc._.blob.polarity < 0:
        # Polaridade de sentimento do texto (-1 negativo a 1 positivo)
        print(f"A review é negativa: {doc._.blob.polarity}")
    elif doc._.blob.polarity > 0:
        print(f"A review é positiva: {doc._.blob.polarity}")
    else:
        print(f"A review é neutra: {doc._.blob.polarity}")
    #print(doc._.blob.subjectivity) # Similar a polaridade (0 (objetivo) a 1 (subjetivo)) que indica o nivel de opinião do texto
    #print(doc._.blob.sentiment_assessments.assessments) # Avaliações de sentimentos para cada frase ou texto
    #print(doc._.blob.ngrams()) # Retorna uma lista de N-gramas