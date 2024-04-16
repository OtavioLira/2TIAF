/* Manipulação Avançada de Objetos
1. Exercício de Propriedades Dinâmicas:

Crie um objeto pessoa com as propriedades nome e idade. Adicione dinamicamente a propriedade profissão ao objeto e defina o valor da profissão.

(2 pontos)
*/

var pessoa = {
    nome: "Otavio",
    idade: 19
}

pessoa["profissao"] = "Programador"

console.log(pessoa)

