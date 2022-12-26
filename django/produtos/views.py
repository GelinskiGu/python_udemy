from django.shortcuts import render

def metodo(request):
    return render(request, 'produtos/index.html')
