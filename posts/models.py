from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import Q



User = settings.AUTH_USER_MODEL


class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            print('test')
            return self.none()
        lookups = Q(user__username__icontains=query)
        return self.filter(lookups)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Post(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    description = models.CharField(max_length=512, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = PostManager()

    

    def like_counter(self):
        return Like.objects.filter(post=self.id).count()

    def comments_to_post(self):
        return Comment.objects.filter(post=self.id).order_by('-created')


    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'id': self.id})


class Comment(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    text = models.CharField(max_length=1024)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:profile', kwargs={'username': self.user})


class Like(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
