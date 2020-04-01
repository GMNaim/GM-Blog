from django.urls import path
from .views import post_list, post_details, post_create, contact
urlpatterns = [
    path('blog-list/', post_list, name='blog-list'),
    path('post/<int:pk>/', post_details, name='post-details'),
    path('post/create/', post_create, name='create-post'),
    path('contact/', contact, name='contact'),
]
