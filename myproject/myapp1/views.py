from django.shortcuts import render

from .models import Film


def index(request):
    films = Film.objects.all()
    data = {
        'films': films
    }
    return render(request, 'films/index.html', context=data)