from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render(request, 'index.html', context_dict)

def about(request):
    return HttpResponse("it's the about section here <br/> <a href='/rango'> index </a>")
