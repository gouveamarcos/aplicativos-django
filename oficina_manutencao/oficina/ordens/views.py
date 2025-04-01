from django.shortcuts import render, redirect
from .models import OrdemServico
from clientes.models import Cliente
from .forms import OrdemServicoForm

def pesquisar_os(request):
    ordens = None
    cpf_digitado = ""

    if request.method == "POST":
        cpf_digitado = request.POST.get("cpf")
        try:
            cliente = Cliente.objects.get(cpf=cpf_digitado)
            ordens = OrdemServico.objects.filter(cliente=cliente)
        except Cliente.DoesNotExist:
            ordens = None

    return render(request, "ordens/pesquisar_os.html", {"ordens": ordens, "cpf_digitado": cpf_digitado})

def abrir_ordem_servico(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = OrdemServicoForm()
    return render(request, 'ordens/abrir_os.html', {'form': form})