from game import Megasena, JogarMegasena

quantidade_de_dezenas = 6
quantidade_de_cartela = 10
ms = Megasena(quantidade_de_dezenas)
class_jogar = JogarMegasena(ms)
isValid = class_jogar.validaQuantidadeDeDezenas()
if isValid:
    class_jogar.gerarJogos(quantidade_de_cartela)
    class_jogar.sortear()
    print(f"Cartela Sorteada..: {class_jogar.getResultado()}")
    cartela_sorteada = class_jogar.resultadoDoSorteio()
    cartelas_jogadas = class_jogar.getJogos()
    jogos_conferidos = class_jogar.confere_cartelas(cartelas_jogadas, cartela_sorteada)
    for jogos in jogos_conferidos:
        print(jogos)
