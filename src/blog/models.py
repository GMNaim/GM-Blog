from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from categories.models import Category

User = get_user_model()


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Postable(TimeStampedModel):
    # ckeditor_uploader component
    message = RichTextField(config_name='special')

    class Meta:
        abstract = True


class Post(Postable):
    """ Post table """
    post_title = models.TextField()  # The form field’s label is set to the verbose_name of the model field, with the first character capitalized.
    posted_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, default='-')
    categories = models.ManyToManyField(Category, related_name='categories')  # there can be more than one category for one post
    tagname = models.TextField(max_length=50, default='')
    overview = models.TextField(max_length=300, default='')
    main_content = models.TextField(default='')  # ckeditor_uploader component...
    featured_post = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='blog_pics/%Y/%m/%d')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.post_title:.50}"

    # def save(self, *args, **kwargs):
    #     """ Fixing the image in a fixed size(height and width) """
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.thumbnail.path)
    #
    #     if img.height > 400 or img.width > 400:
    #         output_size = (400, 400)
    #         img.thumbnail(output_size)
    #         img.save(self.thumbnail.path)

    def get_absolute_url(self):
        """ To avoid hard coding path/url we use this method."""
        return reverse('post-details', kwargs={'pk': self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-created')

    @property
    def comments_count(self):
        return Comment.objects.filter(comment_for_the_post=self).count()

    @property
    def likes_count(self):
        return Like.objects.filter(liked_for_the_post=self).count()


class Like(models.Model):
    liked_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    liked_for_the_post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.liked_for_the_post}: {self.liked_by}"


class Comment(Postable):
    """ Comment table"""
    # commented_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    commented_by = models.CharField(max_length=100, verbose_name='Name')
    commentor_email = models.EmailField(verbose_name='Email')
    comment_for_the_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.commented_by} for post {self.comment_for_the_post}"
