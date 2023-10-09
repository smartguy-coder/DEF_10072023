from django.contrib import admin

# from library.main import models
from . import models

admin.autodiscover()


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'pseudonym']
    list_display = ('name', 'id', 'pseudonym')
    ordering = ('id',)


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'price')
    list_filter = ('author',)
    ordering = ('id',)
    readonly_fields = ('created_at',)


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)

