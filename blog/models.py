from django.urls import reverse
from django.db import models
from django.utils import timezone

# Create your models here.

# post function

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.title

# comment function

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments =True
        self.save()
 
    def get_absolute_url(self):
        return reverse("post_list")


    def __str__(self):
        return self.text