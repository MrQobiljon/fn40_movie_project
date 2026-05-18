from django.urls import path

from .views import all_cinemas, detail_cinema


urlpatterns = [
    path('', all_cinemas, name='all_cinemas'),
    path('cinema/<int:cinema_id>/', detail_cinema, name='detail'),
]