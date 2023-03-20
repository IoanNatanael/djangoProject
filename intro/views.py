from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required()
def first_page(request):
    return HttpResponse("<h3>Hello World</h3>")

@login_required()
def cars(request):
    context = {
        "all_cars": [
            {
                'brand': 'Dacia',
                'color': 'White',
                'year': 2023
            },
            {
                'brand': 'Mini Cooper',
                'color': 'Black',
                'year': 2022
            },
            {
                'brand': 'Audi',
                'color': 'Red',
                'year': 2020
            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)

@login_required()
def series(request):
    movie = {
        'all_series': [
            {
                'movie': 'Lucifer',
                'main_actor': 'Tom Ellis',
                'year': 2016
            },
            {
                'movie': 'Miami Bici',
                'main_actor': 'Matei Dima',
                'year': 2020
            },
            {
                'movie': 'The Survivor',
                'main_actor': 'Harry Haft',
                'year': 2021
            }
        ]
    }
    return render(request, 'intro/list_of_series.html', movie)
