from django.shortcuts import render
from .models import Transacao
from .form import TransacaoForm

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']

    data['now'] = datetime.datetime.now()
    # html = "<html><body></body>It is now %s.</html>" % now
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm()
    data = {}
    data['form'] = form
    return render(request, 'contas/form.html', form)