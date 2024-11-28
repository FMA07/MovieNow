from django.shortcuts import render

# Create your views here.

def catalogo(request):
    context={}
    return render(request, 'pages/catalogo.html')