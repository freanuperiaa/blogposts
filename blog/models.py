from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title[:30]

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])