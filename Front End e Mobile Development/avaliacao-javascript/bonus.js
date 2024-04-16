var Jogador = {
    nome: "Player1",
    lvl: 10,
    hp: 100,
    dano: 10,
    equipamento: ["espada", "arco", "escudo"]
}

var Minion = {
    nome: "Goblin",
    lvl: 1,
    hp: 10,
    dano: 1
}

let {nome: nomeJogador, lvl: nivelJogador, dano: danoJogador} = Jogador
let {nome: nomeMinion, hp: vidaMinion} = Minion

console.log(nomeJogador + " Encontrou o " + nomeMinion) // Encontrou
console.log(nomeJogador + " Atacou o " + nomeMinion + " com a " + Jogador.equipamento.filter((x) => x == "espada") + "\nE " + nomeJogador + " Causou " + danoJogador + " de dano") // Atacou
console.log("HP do "+ nomeMinion + ": " + vidaMinion + ", " + nomeJogador + " Matou o " + nomeMinion) // Matou
console.log(nomeJogador + " Subiu de nivel! " + ", e recebeu uma nova classe: ") // Subiu de nivel
console.log(Jogador['classe'] = "guerreiro")
console.log("Por concluir a fase, seus equipamentos evoluiram: " + Jogador.equipamento.map((x) => x + " raro"))