# Yolo

### O que é

É uma rede neural convolucional (CNN), é o que seria isso? as
CNN, é um algoritmo de computador que tem como objetivo
detectar objetos em tempo real, e qual seria as aplicações
desse algoritmo no dia a dia?

### Aplicações

* Segurânça: Monitoramento de ambientes em tempo real 
* Carros Autônomos: Detecção de pedestres, veículos e outros
obstáculos
* Controle de Estoque: Automatização da contagem e
identificação de produtos em armazém e lojas 
* Reconhecimento de Linguagem de Sinais: tradução em tempo
real de sinais para linguagem escrita ou falada.

### Detecção de Objetos

* A imagem e separada por grid

    * 3 x 3 x 2 x 8: Grid x grid x anchor boxes x bboxes
    parameters 
    * Grid: A imagem é dividida em uma grande retangular
    uniforme
    * Anchor boxes: São caixas que o YOLO  cada célula da
    grade. A ideia é que um desses formatos de caixa se
    ajuste melhor ao objeto real presente naquela área.
    * bboxes parameters: parametros

### Fazendo as predições

* Para cada celula da grade, ele prevê 2 bounding boxes
* Descarte os bounding boxes com baixa probabilidade de conter um objeto
* Para cada classe (pedestr, carro e moto), use non max supression para gerar a predição final

### CP2

1. Carregar um modelo Yolo pré-treinado
2. Testar o modelo Yolo para detectar pessoas
3. Fazer um código para detectar o comportamento das pessoas
em um vídeo de segurânça

Grupo de 2 a 3 pessoas - entrega 01/05