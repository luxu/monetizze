from django.shortcuts import render

from game import Megasena, JogarMegasena

from .forms import MegasenaForm


def index(request):
    template = 'megasena/index.html'
    if request.method == 'POST':
        form = MegasenaForm(request.POST)
        if form.is_valid():
            quantidade_de_dezenas = int(request.POST.get('dezenasPorCartela'))
            cartelas_para_jogar = int(request.POST.get('cartelas'))
            ms = Megasena(quantidade_de_dezenas)
            jogar = JogarMegasena(ms)
            jogar.gerarJogos(cartelas_para_jogar)
            jogar.sortear()
            lista = []
            for nro_da_cartela, cartela in enumerate(jogar.getJogos()):
                contar_numeros_acertados = 0
                nrs_acertados = []
                for nro_acertados in jogar.resultadoDoSorteio():
                    if nro_acertados in cartela:
                        contar_numeros_acertados += 1
                        nrs_acertados.append(nro_acertados)
                if contar_numeros_acertados > 0:
                    dict_cartela = {
                        f'Cartela-{nro_da_cartela+1}': nro_da_cartela+1,
                        'cartela': cartela,
                        'acertos': contar_numeros_acertados,
                        'nros_acertados': nrs_acertados
                    }
                    lista.append(dict_cartela)
            context = {
                'jogos': jogar.getJogos(),
                'qt_de_cartela_do_jogo': len(jogar.getJogos()),
                'resultado': jogar.resultadoDoSorteio(),
                'cartelas_sorteadas': lista,
                'escolher': True
            }
            return render(request, template, context)
    else:
        form = MegasenaForm()
    return render(request, template, {'form': form})
