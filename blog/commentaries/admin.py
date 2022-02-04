from django.contrib import admin

from commentaries.models import Commentaries


@admin.register(Commentaries)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author","text", "created_at")
    fields = ("author","text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("author", "text")