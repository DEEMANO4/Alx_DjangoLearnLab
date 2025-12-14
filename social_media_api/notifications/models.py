from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications', 
    help_text='The user designated to receive the notification.')
    verb = models.CharField(
        max_length=255, help_text='A short description of the action (e.g "commented", "liked", "followed")'
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )
    is_read = models.BooleanField(default=False, db_index=True)

    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actions_peformed', help_text='The user who initiated the action.')

    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} to {self.recipient}"