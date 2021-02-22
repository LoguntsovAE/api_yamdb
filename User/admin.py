from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_full_name', 'role')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'username', 'email')
    empty_value_display = '-'

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'Полное имя'


admin.site.register(User, UserAdmin)
