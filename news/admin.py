from django.contrib import admin
from .models import Article,Tags

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Tags)
