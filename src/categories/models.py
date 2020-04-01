from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=80, unique=True, default='Uncategorised')

    def __str__(self):
        return self.category_name

    def category_wise_post_count(self):
        from blog.models import Post  # importing here because if i import at the top there are some porblem of circular referencing
        return Post.objects.filter(categories=self).count()

# TODO: create subcategories
