from game import Megasena, JogarMegasena


def test_GET_dos_atributos_da_classe_jogarmegasena():
    megasena = Megasena()
    jogar = JogarMegasena(megasena)
    assert jogar.getQuantidadeDeDezenas() == 0
    assert jogar.getResultado() == []
    assert jogar.getTotalJogos() == 0
    assert jogar.getJogos() == []
    assert jogar.getCartela() == []


def test_SET_dos_atributos_da_classe_jogarmegasena():
    megasena = Megasena()
    jogar = JogarMegasena(megasena)
    quantidade_de_dezenas = 6
    numero = 4
    assert jogar.setQuantidadeDeDezenas(quantidade_de_dezenas) is None
    assert jogar.setResultado(numero) is None
    assert jogar.setJogos() is None


def test_valor_valido_para_quantidade_de_dezenas():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.validaQuantidadeDeDezenas() is False


def test_valor_invalido_para_quantidade_de_dezenas():
    quantidade_de_dezenas = 11
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.validaQuantidadeDeDezenas() is False


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


def test_quais_elementos_do_array():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    isValid = jogar.validaQuantidadeDeDezenas()
    if isValid:
        jogar.setCartela()
        assert len(jogar.getCartela()) == quantidade_de_dezenas


def test_quantidade_de_jogos():
    quantidade_de_dezenas = 10
    quantidade_de_cartela = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    jogar._gerarCartelas(quantidade_de_dezenas)
    jogar.gerarJogos(quantidade_de_cartela)
    assert jogar.getTotalJogos() == quantidade_de_cartela


def test_sorteio():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    jogar.sortear()
    assert len(jogar.resultadoDoSorteio()) == 6
