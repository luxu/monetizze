from game import Megasena, JogarMegasena

quantidade_de_dezenas = 5
ms = Megasena(quantidade_de_dezenas)
jogar = JogarMegasena(ms)
cartelas_para_jogar = 4
for i in range(cartelas_para_jogar):
    jogar.gerarCartelas()
    jogar.setJogos()
jogar.sortear()
for nro_da_cartela, cartela in enumerate(jogar.getJogos()):
    print(f'Cartela-{nro_da_cartela+1}: {cartela}')
    print(f'Números Sorteados..: {jogar.resultadoDoSorteio()}')
    contar_numeros_acertados = 0
    for nro_acertados in jogar.resultadoDoSorteio():
        if nro_acertados in cartela:
            print(nro_acertados)
            contar_numeros_acertados += 1
    if contar_numeros_acertados > 0:
        print(f'Acertou {contar_numeros_acertados} números da Cartela-{nro_da_cartela+1}\n{"*"*50}')
    else:
        print(f'Não houve acertou na Cartela-{nro_da_cartela + 1}\n{"*" * 50}')
