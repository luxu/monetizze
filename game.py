import random


class Megasena:
    def __init__(self, quantidade_de_dezenas=0):
        self._quantidade_de_dezenas = quantidade_de_dezenas
        self._jogos = []
        self._resultado = []
        self._total_de_jogos = []

    def quantidadeDeDezenas(self):
        if self._quantidade_de_dezenas in range(6, 11):
            return True
        return False


class JogarMegasena:
    def __init__(self, megasena):
        self.megasena = megasena
        self.cartela = []

    def getQuantidadeDeDezenas(self):
        return self.megasena._quantidade_de_dezenas

    def setQuantidadeDeDezenas(self, quantidade_de_dezenas):
        self.megasena.quantidade_de_dezenas = quantidade_de_dezenas

    def getCartela(self):
        return self.cartela

    def setCartela(self):
        cartelas = self._gerarCartelas(
            self.getQuantidadeDeDezenas()
        )
        self.cartela = cartelas

    def setTotalDeJogos(self, total_de_jogos):
        self.megasena.total_de_jogos = total_de_jogos

    def getTotalDeJogos(self):
        return self.megasena.total_de_jogos

    def setJogos(self):
        self.megasena._jogos.append(self.getCartela())
        self.esvaziarCartela()

    def getJogos(self):
        return self.megasena._jogos

    def getTotalJogos(self):
        return len(self.megasena._jogos)

    def getResultado(self):
        return self.megasena._resultado

    def setResultado(self, numero):
        self.megasena._resultado.append(numero)
        self.megasena._resultado.sort()

    def getArrayDeDezenas(self):
        cartela = []
        return cartela

    def getQuantidadeDeTotalJogos(self):
        return self.megasena.total_de_jogos

    def validaQuantidadeDeDezenas(self):
        return self.megasena.quantidadeDeDezenas()

    def _gerarCartelas(self, qtde_de_dezenas):
        nv_cartela = []
        cont = 0
        while cont < qtde_de_dezenas:
            try:
                numero = self.gerarNumeros(nv_cartela)
                if numero > 0:
                    nv_cartela.append(numero)
                    cont += 1
            except TypeError:
                pass
        return nv_cartela

    def gerarNumeros(self, cartelas):
        numero = random.randint(1, 60)
        cartelas.sort()
        if numero not in cartelas:
            return numero

    def sortear(self):
        cont = 0
        while cont < 6:
            try:
                numero = self.gerarNumeros(self.getResultado())
                if numero > 0:
                    self.setResultado(numero)
                    cont += 1
            except TypeError:
                pass

    def gerarJogos(self, quantidade_de_cartela):
        for cartela in range(quantidade_de_cartela):
            self.setCartela()
            self.setJogos()

    def esvaziarCartela(self):
        self.cartela = []

    def resultadoDoSorteio(self):
        return self.getResultado()
