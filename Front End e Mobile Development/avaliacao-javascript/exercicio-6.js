/* Manipulação Avançada de Objetos

3. Exercício de Spread Operator:

Crie dois arrays array1 e array2. Utilize o spread operator para criar um terceiro array array3 contendo todos os elementos de array1 e array2.

(2 pontos)

*/

const array1 = [1, 2, 3]
const array2 = [4, 5, 6]

const array3 = [...array1, ...array2]

console.log(array3)
