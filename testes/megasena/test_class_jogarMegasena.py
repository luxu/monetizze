from game import Megasena, JogarMegasena


def test_valor_valido_para_quantidade_de_dezenas():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.megasena.validaQuantidadeDeDezenas() is False


def test_valor_invalido_para_quantidade_de_dezenas():
    quantidade_de_dezenas = 11
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.megasena.validaQuantidadeDeDezenas() is False


def test_inserir_total_de_jogos():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    jogar.setTotalDeJogos(11)
    assert jogar.getTotalDeJogos() == 11


def test_retornar_se_eh_um_array():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.getCartela() == []


def test_se_array_tem_tamanho_de_quantidade_de_dezenas_definido():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.validaCartela() is True


def test_quais_elementos_do_array():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    if jogar.validaCartela() is True:
        jogar.gerarCartelas()
        print()
    assert len(jogar.getCartela()) == quantidade_de_dezenas


def test_quantidade_de_jogos():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    jogar.gerarCartelas()
    jogar.setJogos()
    assert jogar.getTotalJogos() == 1


def test_sorteio():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    jogar.sortear()
    assert len(jogar.resultadoDoSorteio()) == 6
