from django.contrib import admin
from .models import Blogs,Comment

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Comment)
