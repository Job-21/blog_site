from django.db import models

# Create your models here.
class BlogDetails(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    blog_text = models.TextField()
    blog_date = models.DateField(auto_now_add=True)