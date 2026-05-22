from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea
from django.utils.safestring import mark_safe

from .models import Cinema, Actor, Comment

admin.site.site_header = "FN40"
admin.site.site_title = "fn40"
admin.site.login_template = "admin/my_login.html"
admin.site.logout_template = "admin/logout.html"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ("user",)

    formfield_overrides = {
        TextField: {
            "widget": Textarea(attrs={
                "rows": 2,
                "cols": 40,
            })
        },
    }

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for instance in instances:
            # yangi comment bo‘lsa user biriktiriladi
            if not instance.pk and not instance.user:
                instance.user = request.user

            instance.save()

        formset.save_m2m()


@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'published_year', 'created', 'my_test_func', 'time_check', 'get_image', 'video')
    list_display_links = ('name',)
    list_filter = ('published_year',)
    list_editable = ('published_year',)
    search_fields = ('name', 'annotation', 'published_year', 'poster')
    # fields = (
    #     ('name', 'annotation'),
    #     ('poster', 'video'),
    #     ('published_year',)
    # )
    fieldsets = [
        (
            "Asosiy",
            {
                'fields': ['name', 'annotation'],
            }
        ),
        (
            "Media",
            {
                "fields": ["poster", "video"],
                "classes": ["collapse"],
                "description": "Bu yerda rasm va video bo'ladi!"
            }
        ),
        (
            "Taqdim etilgan",
            {
                "fields": ['published_year'],
                "classes": ["collapse"]
            }
        )
    ]
    inlines = [
        CommentInline
    ]

    @admin.display(description="Rasmi")
    def get_image(self, cinema):
        if cinema.poster:
            return mark_safe(f'<img src="{cinema.poster.url}" width="150px">')
        else:
            return '-'

    @admin.display(boolean=True, description="Tekin")
    def my_test_func(self, obj):
        if obj.published_year >= 2020:
            return False
        return True

    @admin.display(description="Vaqt bo'ldi")
    def time_check(self, obj):
        return f"{2026 - obj.published_year} yil bo'ldi!!!"



@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass
