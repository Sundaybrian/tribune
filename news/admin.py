from django.contrib import admin
from .models import Editor,Article,Tags

# Register your models here.

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(Tags)
