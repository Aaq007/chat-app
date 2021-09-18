import uuid

from authentication.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


def validate_message(message):
    if message is None or message.strip() == '':
        raise ValidationError('Message is empty', params={'message': message})


class Message(models.Model):
    id = models.UUIDField(primary_key=True, null=False,
                          blank=False, default=uuid.uuid3, editable=False)
    user = models.ForeignKey(to=User, blank=False,
                             null=False, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(validators=(validate_message,))
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def fetch_last_25_messages(self):
        return Message.objects.order_by('-created_at').all()[:25]
