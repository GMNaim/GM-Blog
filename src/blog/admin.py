from django.contrib import admin
from .models import Post, Like, Comment


# class PostImageInline(admin.StackedInline):
#     model = PostImage


class PostAdmin(admin.ModelAdmin):
    # inlines = [PostImageInline]
    list_display = ('id', 'post_title', 'posted_by', 'is_approved', 'featured_post', 'publish_date', 'created',)
    list_display_links = ('post_title', 'id')
    list_editable = ('is_approved', 'featured_post')
    fields = ('post_title', 'overview', 'posted_by', 'main_content', 'categories', 'is_approved', 'featured_post',
              'slug', 'thumbnail', 'publish_date')
    search_fields = ('post_title', 'message', 'publish_date')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'liked_for_the_post')
    list_display_links = ('id', 'liked_for_the_post',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_for_the_post')
    list_display_links = ('id', 'comment_for_the_post')


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
