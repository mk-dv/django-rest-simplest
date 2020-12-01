from django.contrib import admin

from .models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
