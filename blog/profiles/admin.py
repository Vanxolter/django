from django.contrib import admin

from profiles.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name","surname", "age", "sex", 'email')
    fields = ("name","surname",'email', "age", "sex")
    readonly_fields = ("created_at",)
    search_fields = ("name", "surname", "email")