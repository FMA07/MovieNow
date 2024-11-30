from django.shortcuts import render

# Create your views here.

def reserva(request):
    context={}
    return render(request, 'pages/reserva.html', context)
