from django.shortcuts import render

from .models import Cinema


def all_cinemas(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'movie/all_cinemas.html', context)


def detail_cinema(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    return render(request, 'movie/detail.html', {'cinema': cinema})