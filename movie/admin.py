from django.contrib import admin

from .models import Cinema, Actor

admin.site.register([Cinema, Actor])