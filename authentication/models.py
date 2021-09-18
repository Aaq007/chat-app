from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    last_seen = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    online = models.BooleanField(default=False, null=False, blank=False)
