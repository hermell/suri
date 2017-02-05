from django.db import models
from django.utils import timezone

class User(models.Model):

    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "TB_USR_INFO"


