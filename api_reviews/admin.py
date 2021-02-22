from django.contrib import admin

from .models import Title
from .models.category import Category
from .models.comment import Comment
from .models.genre import Genre
from .models.review import Review


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Category, CategoryAdmin)


class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Genre, GenreAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'text', 'pub_date', 'review_id')
    list_filter = ('pub_date',)
    search_fields = (
        'author__first_name',
        'author__last_name',
        'author__username',
        'text'
    )
    autocomplete_fields = ('author',)
    raw_id_fields = ('review',)
    empty_value_display = '-'


admin.site.register(Comment, CommentAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'text', 'pub_date', 'score')
    list_filter = ('score', 'pub_date')
    search_fields = (
        'title__name',
        'text',
        'author__username',
        'author__first_name',
        'author__last_name'
    )
    autocomplete_fields = ('author', 'title')
    empty_value_display = '-'


admin.site.register(Review, ReviewAdmin)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'genre_list', 'category')
    list_filter = ('genre', 'category')
    search_fields = ('name', 'year')
    autocomplete_fields = ('category',)
    empty_value_display = '-'

    def genre_list(self, obj):
        genres = obj.genre.all()
        if genres:
            genres_list = ', '.join([genre.name for genre in genres[:2]])
            if len(genres) > 2:
                genres_list += ' и т.д.'
            return genres_list

        return '-'

    genre_list.short_description = 'Жанры'


admin.site.register(Title, TitleAdmin)
