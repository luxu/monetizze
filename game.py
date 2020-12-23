import random


class Megasena:
    def __init__(self, quantidade_de_dezenas=0):
        self.quantidade_de_dezenas = quantidade_de_dezenas
        self.jogos = []
        self.resultado = []

    def __str__(self):
        return 'Mega da Virada'

    def validaQuantidadeDeDezenas(self):
        if self.quantidade_de_dezenas in range(6, 11):
            return True
        return False


class JogarMegasena:
    def __init__(self, megasena):
        self.megasena = megasena
        self.cartela = []
        self.total_de_jogos = []

    def getQuantidadeDeDezenas(self):
        return self.megasena.quantidade_de_dezenas

    def setQuantidadeDeDezenas(self, quantidade_de_dezenas):
        self.megasena.quantidade_de_dezenas = quantidade_de_dezenas

    def getCartela(self):
        return self.cartela

    def setCartela(self, numero):
        self.cartela.append(numero)

    def setTotalDeJogos(self, total_de_jogos):
        self.megasena.total_de_jogos = total_de_jogos

    def getTotalDeJogos(self):
        return self.megasena.total_de_jogos

    def setJogos(self):
        self.megasena.jogos.append(self.getCartela())
        self.esvaziarCartela()

    def getJogos(self):
        return self.megasena.jogos

    def getTotalJogos(self):
        return len(self.megasena.jogos)

    def getArrayDeDezenas(self):
        cartela = []
        return cartela

    def gerarCartelas(self):
        cont = 0
        while cont < self.getQuantidadeDeDezenas():
            numero = random.randint(1, 60)
            if numero not in self.getCartela():
                self.setCartela(numero)
                cont += 1
        self.cartela.sort()

    def validaCartela(self):
        return self.megasena.validaQuantidadeDeDezenas()

    def getQuantidadeDeTotalJogos(self):
        return self.megasena.total_de_jogos

    def esvaziarCartela(self):
        self.cartela = []

    def resultadoDoSorteio(self):
        return self.getResultado()

    def sortear(self):
        cont = 0
        while cont < 6:
            numero = random.randint(1, 60)
            if numero not in self.getResultado():
                self.setResultado(numero)
                cont += 1
        self.megasena.resultado.sort()

    def getResultado(self):
        return self.megasena.resultado

    def setResultado(self, numero):
        self.megasena.resultado.append(numero)
