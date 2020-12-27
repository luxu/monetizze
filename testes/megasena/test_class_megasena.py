from game import Megasena, JogarMegasena


def test_existem_atributos_de_classe():
    ms = Megasena()
    assert ms._quantidade_de_dezenas == 0
    assert ms._resultado == []
    assert ms._total_de_jogos == []
    assert ms._jogos == []


def test_quantidade_de_dezenas_valida():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.validaQuantidadeDeDezenas() is True


def test_quantidade_de_dezenas_invalida():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    jogar = JogarMegasena(ms)
    assert jogar.validaQuantidadeDeDezenas() is False
