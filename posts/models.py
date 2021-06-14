from django.db import models
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.TextField(null = True, blank = True)
    likes = models.ManyToManyField(User, related_name="post_like", null=True, blank=True)
    disLikes = models.ManyToManyField(User, related_name="post_dislike",null=True,blank=True)
    pub_date = models.DateTimeField(default= timezone.now)

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.author} / {self.status}"

    @property
    def like_count(self):
        count = self.likes.count()
        return count

    @property
    def dis_like_count(self):
        count = self.disLikes.count()
        return count
        
class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ManyToManyField(User, related_name="post_comments")
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.post} // {self.comment}"