from django.contrib import admin

# from library.main import models
from . import models

admin.autodiscover()


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'pseudonym']
    list_display = ('name', 'id')
    ordering = ('id',)


admin.site.register(models.Author, AuthorAdmin)

