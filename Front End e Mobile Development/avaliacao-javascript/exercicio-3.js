/*
3. Exercício de Reduce:

Dado o array de números [5, 10, 15, 20, 25], utilize o método reduce para calcular a soma de todos os números do array.

(1 ponto)
*/
const array = [5,10,15,20,25]
const valorInicial = 0
const somaComValorInicial = array.reduce(
    (acumulador, valorAtual) => acumulador + valorAtual, valorInicial,
)

console.log(somaComValorInicial)