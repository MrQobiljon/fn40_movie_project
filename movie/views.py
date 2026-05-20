from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Cinema, CinemaLike


def all_cinemas(request):
    cinemas = Cinema.objects.all()
    if request.user.is_authenticated:
        for cinema in cinemas:
            if CinemaLike.objects.filter(cinema=cinema, user=request.user).exists():
                cinema.like = True
            else:
                cinema.like = False
            cinema.save()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'movie/all_cinemas.html', context)


def detail_cinema(request, cinema_id):
    cinema = Cinema.objects.get(pk=cinema_id)
    return render(request, 'movie/detail.html', {'cinema': cinema})


@login_required(login_url='all_cinemas')
def create_like(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    like, created = CinemaLike.objects.get_or_create(cinema=cinema, user=request.user)
    if not created:
        like.delete()
    return redirect('all_cinemas')


