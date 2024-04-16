/* Manipulação Avançada de Objetos
2. Exercício de Destruturação:

Dado o objeto produto com as propriedades nome, preco e quantidade, utilize a desestruturação para extrair o nome e o preço do produto.

(2 pontos)
*/

var produto = {
    nome: "Garrafa TOP 1000",
    preco: 150,
    quantidade: 10
}

var { nome, preco } = produto

console.log(nome)
console.log(preco)