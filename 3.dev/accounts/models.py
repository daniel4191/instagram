from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    # validators=[]로 숫자만 유효성 검사로 하게끔
    zipcode = models.CharField(max_length=6, )
