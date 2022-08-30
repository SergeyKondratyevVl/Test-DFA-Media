from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def upload_to(instance, filename):
    return f'profiles/{instance.to_user_id}/{filename}'

class Gallery(models.Model):
    to_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='photo', unique=False)
    profile_photo = models.ImageField(upload_to=upload_to, null=True, verbose_name='Photo')
    changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Photo of {self.to_user.username}, changed {self.changed}"
    