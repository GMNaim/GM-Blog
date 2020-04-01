from django.shortcuts import render
from .models import HomePageSettings, Gallery
import random
from blog.models import Post


def home(request):
    # home_page_info = HomePageSettings.objects.all().last()  # getting the last row of the table by using last()
    # gallery = Gallery.objects.all().last()
    home_page_info = HomePageSettings.objects.get(active=True)  # getting the record if the active is true
    gallery = Gallery.objects.get(active=True)
    featured_post = Post.objects.filter(is_approved=True).filter(featured_post=True)[:3]
    latest_post = Post.objects.filter(is_approved=True).order_by('-pk')[:3]
    print('======================== latest posts are: ')
    print(latest_post)

    context = {'home_page_info': home_page_info,
               'gallery': gallery,
               'featured_post': featured_post,
               'latest_post': latest_post,
               }
    return render(request, 'frontend/mainapp/home.html', context)
