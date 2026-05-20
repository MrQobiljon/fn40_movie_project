from django.urls import path

from .views import all_cinemas, detail_cinema, create_like


urlpatterns = [
    path('', all_cinemas, name='all_cinemas'),
    path('cinema/<int:cinema_id>/', detail_cinema, name='detail'),
    path('add/bookmark/<int:cinema_id>/', create_like, name='create_like'),
]