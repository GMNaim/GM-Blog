from django.urls import path
from .views import post_list, post_details, post_create, contact, tagged_post, categorised_posts
urlpatterns = [
    path('blog-list/', post_list, name='blog-list'),
    path('post/<int:pk>/', post_details, name='post-details'),
    path('post/create/', post_create, name='create-post'),
    path('posts/category/<str:category_name>', categorised_posts, name='categorized-post'),

    path('posts/tag/<str:tag_name>', tagged_post, name='tagged-post'),

    path('contact/', contact, name='contact'),
]
