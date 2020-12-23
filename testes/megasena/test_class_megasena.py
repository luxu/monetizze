from game import Megasena


def test_nome_da_classe():
    ms = Megasena()
    assert str(ms) == 'Mega da Virada'


def test_existem_atributos_de_classe():
    ms = Megasena()
    assert ms.resultado == []
    assert ms.jogos == []


def test_quantidade_de_dezenas_valida():
    quantidade_de_dezenas = 10
    ms = Megasena(quantidade_de_dezenas)
    assert ms.validaQuantidadeDeDezenas() is True


def test_quantidade_de_dezenas_invalida():
    quantidade_de_dezenas = 5
    ms = Megasena(quantidade_de_dezenas)
    assert ms.validaQuantidadeDeDezenas() is False
