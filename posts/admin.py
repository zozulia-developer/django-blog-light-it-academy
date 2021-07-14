from django.contrib import admin

from .models import Post, Category


class PostCategoryInline(admin.TabularInline):  # изменить количество категорий
    model = Post.categories.through


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [
        PostCategoryInline
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
