from django.contrib import admin

from .models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_dispaly = [
        "user",
        "book",
        "text",
        "datetime_created",
    ]

admin.site.register(MdlBook)
admin.site.register(Comment, CommentAdmin)
