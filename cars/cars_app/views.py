from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def test(request):
    print(request.POST.get("test"))
    return render(request, 'pages/index.html')