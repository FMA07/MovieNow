from django.shortcuts import render

# Create your views here.

def arriendo(request):
    context={}
    return render(request, 'pages/arriendo.html', context)