from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_joined = models.DateTimeField('date_joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    email_verified = models.BooleanField('email_verified', default=False)

    class Meta(object):
        unique_together = ('email',)


class Images(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField('image_url', max_length=256)
    # short_image_url = models.CharField('short_image_url', max_length=128)