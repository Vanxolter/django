from django.contrib import admin

from comments.models import Commentaries


@admin.register(Commentaries)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created", "updated")
    fields = ("name", "email", "created", "updated", "body")
    readonly_fields = ("created", "updated")
    search_fields = ("name", "email", "created")
