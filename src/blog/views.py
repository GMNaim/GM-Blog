from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from categories.models import Category
from .forms import PostCreationForm, CommentForm
from mainapp.models import HomePageSettings


def post_list(request):
    """Showing the list of post. and the pagination """
    home_page_info = HomePageSettings.objects.get(active=True)  # if the active option is true then get the row
    latest_post = Post.objects.filter(is_approved=True).order_by('-pk')[:3]  # getting the last 3 post form the table
    post_list = Post.objects.order_by('-created').filter(is_approved=True)  # get all post if it is approved
    # paginator works...
    paginator = Paginator(post_list, 2)  # giving the post items and telling how many items can put in one page
    page = request.GET.get('page')  # getting the page object from the request
    post_list_with_page_number = paginator.get_page(page)  # getting current page number like: <Page 1 of 3> this way

    """
    print('paged_post_list: ', post_list_with_page_number)
    print(type(post_list_with_page_number))
    print(post_list_with_page_number.has_other_pages())
    """
    # getting categories
    categories = Category.objects.all()
    # print(categories, 'categories==========')



    context = {'home_page_info': home_page_info,
               'latest_post': latest_post,
               'post_list_with_page_number': post_list_with_page_number,
               'categories': categories
               }

    # print('===================================== TESTING ===========================================')
    # for post in post_list:
    #     print(post.post_title)
    # print('body====', request.body)
    # print('content_params====', request.content_params)
    # print('content_type====', request.content_type)
    # print('cookies=====', request.COOKIES)
    # # for k, v in request.META.items():
    # #     print(f'{k}=======', v)
    # print('get_port====', request.get_port())
    # print('method====', request.method)
    # print(paginator.orphans)
    # print(paginator.object_list)
    # print(paginator.page_range)
    # print()
    # print('=========================================================================================')

    return render(request, "frontend/blog/blog_list.html", context)


def tagged_post(request, tag_name):
    """Showing the list of tagged post. and the pagination """
    home_page_info = HomePageSettings.objects.get(active=True)  # if the active option is true then get the row
    latest_post = Post.objects.filter(is_approved=True).order_by('-pk')[:3]  # getting the last 3 post form the table
    tagged_post_list = Post.objects.order_by('-created').filter(tagname__contains=tag_name).filter(is_approved=True)  # get all post if it is approved
    # paginator works...
    paginator = Paginator(tagged_post_list, 4)  # giving the post items and telling how many items can put in one page
    page = request.GET.get('page')  # getting the page object from the request
    post_list_with_page_number = paginator.get_page(page)  # getting current page number like: <Page 1 of 3> this way
    print('-------------------------------------------------------------')

    # getting categories
    categories = Category.objects.all()

    context = {'home_page_info': home_page_info,
               'latest_post': latest_post,
               'post_list_with_page_number': post_list_with_page_number,
               'categories': categories
               }

    return render(request, "frontend/blog/tagged_post.html", context)


def categorised_posts(request, category_name):
    """Showing the list of categorised post. and the pagination """
    home_page_info = HomePageSettings.objects.get(active=True)  # if the active option is true then get the row
    latest_post = Post.objects.filter(is_approved=True).order_by('-pk')[:3]  # getting the last 3 post form the table

    category = Category.objects.get(category_name=category_name)
    print('----------====================================-----------------')
    print(category, 'cateorsdfdsfdsdddddddddddddddddddddddddddddddddddddddddddddddddddd')

    categorised_post_list = Post.objects.filter(categories=category).filter(is_approved=True).order_by('-created')  # get all post if it is approved

    # paginator works...
    paginator = Paginator(categorised_post_list, 4)  # giving the post items and telling how many items can put in one page
    page = request.GET.get('page')  # getting the page object from the request
    post_list_with_page_number = paginator.get_page(page)  # getting current page number like: <Page 1 of 3> this way

    # getting categories
    categories = Category.objects.all()

    context = {'home_page_info': home_page_info,
               'latest_post': latest_post,
               'post_list_with_page_number': post_list_with_page_number,
               'categories': categories,

               }

    return render(request, "frontend/blog/categorized_posts.html", context)


def post_details(request, pk):
    home_page_info = HomePageSettings.objects.get(active=True)  # if the active option is true then get the row
    latest_post = Post.objects.all().order_by('-pk')[:3]
    # getting the get_post
    get_post = get_object_or_404(Post, id=pk)
    print('post in detail view = ', get_post)
    print('post tags in detail view = ', get_post.tagname)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print('form is valid======')
            new_comment = comment_form.save(commit=False)  # Create Comment object but don't save to database yet
            new_comment.comment_for_the_post = get_post
            new_comment.save()
            print('comment is saved -------------')
            return redirect('post-details', pk=get_post.id)
    else:
        comment_form = CommentForm()

    # Getting the next and previous post. first checking the posts are approved or not then filtering those post
    # whose ids are greater than that post then ordering those post by id and taking the first post as the next post.
    next_post = Post.objects.filter(is_approved=True).filter(id__gt=get_post.id).order_by('id').first()
    # print('---------------------next post==== ', next_post)
    previous_post = Post.objects.filter(is_approved=True).filter(id__lt=get_post.id).order_by('id').last()
    # print('-----------------previous post==== ', previous_post)

    # getting comments
    comments = Comment.objects.filter(comment_for_the_post=pk)
    # print('comments == ', comments)
    # getting categories
    categories = Category.objects.all()

    if get_post.tagname == '':
        tag_list = ''
    else:
        tag_list = get_post.tagname.split(',')

    context = {'home_page_info': home_page_info,
               'latest_post': latest_post,
               'post': get_post,
               'previous_post': previous_post,
               'next_post': next_post,
               'comments': comments,
               'categories': categories,
               'comment_form': comment_form,
               'tag_list': tag_list
               }

    return render(request, 'frontend/blog/individual_post.html', context)


@login_required
def post_create(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    posted_by = request.user
    if request.method == 'POST':
        post_title = request.POST['post_title']
        # categories = dict(request.POST)['post_categories']  # We can use this method also to get the list value
        categories = request.POST.getlist('post_categories')  # also this way is okay to get list
        post_overview = request.POST['post_overview']
        main_content = request.POST['post_mainContent']
        tags = request.POST['post_tags']
        print(tags, '-------==========----------=========------======')
        thumbnail = request.FILES.get('post_thumbnail')
        # print(post_title, categories, post_overview, main_content, thumbnail)
        # print('imageeeeeeeeee=================', thumbnail)
        # print(f'''  {request.POST}
        #             -----------Image file {request.FILES}''')

        # ========== POST VALIDATION =============
        if post_title.strip() == '':
            context = {
                "categories": Category.objects.all(),
                "post_overview": post_overview,
                "main_content": main_content,
                "tags": tags,
            }
            messages.error(request, "Post title can't be empty!")
            return render(request, 'backend/blog/create_post.html', context)

        elif post_overview.strip() == '':
            context = {
                "categories": Category.objects.all(),
                "post_title": post_title,
                "main_content": main_content,
                "tags": tags,

            }
            messages.error(request, "Post overview can't be empty!")
            return render(request, 'backend/blog/create_post.html', context)

        elif main_content.strip() == '':
            context = {
                "categories": Category.objects.all(),
                "post_overview": post_overview,
                "post_title": post_title,
                "tags": tags,
            }
            # print(context.values(), '-------value of context')
            messages.error(request, "Post main content can't be empty!")
            return render(request, 'backend/blog/create_post.html', context)

        elif len(categories) == 0:  # using len() as categories return a list object
            context = {
                "categories": Category.objects.all(),
                "post_overview": post_overview,
                "post_title": post_title,
                "main_content": main_content,
                "tags": tags,

            }
            # print(context.values(), '-------value of context')

            messages.error(request, "Select at least one category!")
            return render(request, 'backend/blog/create_post.html', context)
        elif tags.strip() == '':
            context = {
                "categories": Category.objects.all(),
                "post_overview": post_overview,
                "post_title": post_title,
                "main_content": main_content,
            }
            # print(context.values(), '-------value of context')
            messages.error(request, "Please give some tag name for the post")
            return render(request, 'backend/blog/create_post.html', context)

        elif thumbnail == '':
            messages.error(request, "Please select a thumbnail for you post")
            return render(request, 'backend/blog/create_post.html', context)

        else:
            try:
                new_post = Post.objects.create(post_title=post_title,
                                               posted_by=posted_by,
                                               overview=post_overview,
                                               main_content=main_content,
                                               thumbnail=thumbnail,
                                               tagname=tags)
                new_post.categories.set(categories)  # setting categories externally cause it is many to many field

                new_post.save()
                print('================post created', new_post)
                messages.success(request, 'Your post is created successfully!')
                return redirect('post-details', pk=new_post.id)
            except Exception as e:
                print('Exception ============================================================= ', e)
                messages.error(request, 'There is some problem to create the post!')

    return render(request, 'backend/blog/create_post.html', context)


def contact(request):
    home_page_info = HomePageSettings.objects.get(active=True)  # if the active option is true then get the row
    latest_post = Post.objects.all().order_by('-pk')[:3]

    context = {'home_page_info': home_page_info,
               'latest_post': latest_post}
    return render(request, 'frontend/blog/contact.html', context)
