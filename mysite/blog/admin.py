from django.contrib import admin
from .models import Post, Comment

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "create_at"]
    list_filter = ["create_at", "name"]
    search_fields = ["name", "body"]
    raw_id_fields = ["post"]
    date_hierarchy = "create_at"
    ordering = ["-create_at", "name"]
