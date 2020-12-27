from game import Megasena, JogarMegasena

quantidade_de_dezenas = 6
quantidade_de_cartela = 100
ms = Megasena(quantidade_de_dezenas)
class_jogar = JogarMegasena(ms)
isValid = class_jogar.validaQuantidadeDeDezenas()
if isValid:
    class_jogar.gerarJogos(quantidade_de_cartela)
    class_jogar.sortear()
    for nro_da_cartela, cartela in enumerate(class_jogar.getJogos()):
        contar_numeros_acertados = 0
        guardar_numeros_acertados = []
        for nro_acertados in class_jogar.resultadoDoSorteio():
            if nro_acertados in cartela:
                guardar_numeros_acertados.append(nro_acertados)
                contar_numeros_acertados += 1
        if contar_numeros_acertados > 0:
            print(
                f'Acertou {contar_numeros_acertados} ({guardar_numeros_acertados}) '
                f'número(s) da Cartela-{nro_da_cartela+1}\n{"*"*50}'
            )
