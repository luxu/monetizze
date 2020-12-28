from django.shortcuts import render

from game import Megasena, JogarMegasena

from .forms import MegasenaForm


def index(request):
    template = "megasena/index.html"
    if request.method == "POST":
        form = MegasenaForm(request.POST)
        if form.is_valid():
            quantidade_de_dezenas = int(request.POST.get("dezenasPorCartela"))
            cartelas_para_jogar = int(request.POST.get("cartelas"))
            ms = Megasena(quantidade_de_dezenas)
            jogar = JogarMegasena(ms)
            isValid = jogar.validaQuantidadeDeDezenas()
            if isValid:
                jogar.gerarJogos(cartelas_para_jogar)
                jogar.sortear()
                cartela_sorteada = jogar.resultadoDoSorteio()
                cartelas_jogadas = jogar.getJogos()
                jogos_conferidos = jogar.confere_cartelas(
                    cartelas_jogadas, cartela_sorteada
                )
                context = {
                    "jogos": cartelas_jogadas,
                    "qt_de_cartela_do_jogo": len(cartelas_jogadas),
                    "resultado": cartela_sorteada,
                    "cartelas_sorteadas": jogos_conferidos,
                    "escolher": True,
                }
                return render(request, template, context)
    else:
        form = MegasenaForm()
    return render(request, template, {"form": form})
