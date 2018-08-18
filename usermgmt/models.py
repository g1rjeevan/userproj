from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=50)
    parent = models.CharField(blank=True, max_length=50)
    is_featured = models.BooleanField(default=False)
    image = models.FileField(upload_to=user_directory_path, null=True)
    is_active = models.BooleanField(default=False)
    description = models.CharField(default="No Description", max_length=150)
