from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.safestring import mark_safe


class Actor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="F.I.O")
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Tug'ilgan yili")
    photo = models.ImageField(upload_to='actors/', null=True, blank=True, verbose_name="Rasmi")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Aktor'
        verbose_name_plural = 'Aktorlar'
        ordering = ['-full_name']


class Cinema(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    poster = models.ImageField(upload_to='movie/images/', null=True, blank=True, verbose_name="Rasmi")
    video = models.FileField(
        upload_to='movie/cinemas/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['mp4', 'mov', 'avi'],
                                                                message="Faqatgina mp4, mov, avi formatlariga ruxsat berilgan!")],
        verbose_name="Video"
    )
    annotation = models.TextField(null=True, blank=True, verbose_name="Tavsif")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qachon qo'shilgani")
    published_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Taqdim etilgan yili"
    )
    actors = models.ManyToManyField(Actor, verbose_name="Aktorlar")

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"

    def __str__(self):
        return self.name

    # @admin.display(description="Rasmi")
    # def get_image(self):
    #     if self.poster:
    #         return mark_safe(f'<img src="{self.poster.url}" width="150px">')
    #     else:
    #         return '-'
    #

class CinemaLike(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text