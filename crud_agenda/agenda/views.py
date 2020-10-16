from django.shortcuts import render, redirect
from .forms import FormContato
from .models import Contato
from .filters import ContatoFilter


# Create your views here.

def lista_Contatos(request):  # tratar o show
    contatos = Contato.objects.all()
    myFilter = ContatoFilter(request.GET, queryset=Contato.objects.all())
    contatos = myFilter.qs
    context = {'lista_contatos': contatos, 'myFilter': myFilter}
    return render(request, "agenda/lista_contato.html", context)


def form_Contatos(request, id=0):  # tratar insert e update
    if request.method == "GET":
        if id==0:
            form = FormContato()
        else:
            contato = Contato.objects.get(pk=id)
            form = FormContato(instance=contato)
        return render(request, "agenda/form_contato.html", {'form': form})
    else:
        if id == 0:
            form = FormContato(request.POST)
        else:
            contato = Contato.objects.get(pk=id)
            form = FormContato(request.POST, instance=contato)
        if form.is_valid():
            form.save()
        return redirect('/agenda/lista')


def deletar_Contatos(request, id):  # tratar o delete
    contato = Contato.objects.get(pk=id)
    contato.delete()
    return redirect('/agenda/lista')
