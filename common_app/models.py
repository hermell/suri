from django.db import models
from django.utils import timezone

class Menu(models.Model):

    KIND_OF_MENU = (
        ('T', 'TOP'),
        ('L', 'LEFT'),
    )

    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    level = models.DecimalField(max_digits=10, decimal_places=0)
    kind = models.CharField(max_length=1, choices=KIND_OF_MENU)
    ordered = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    thumbnail = models.CharField(max_length=30, blank=True)
    href_attr = models.CharField(max_length=30, blank=True)
    register_date = models.DateTimeField(default=timezone.now)
    register_id = models.CharField(max_length=30, default='ADMIN')
    update_date = models.DateTimeField(default=timezone.now)
    update_id = models.CharField(max_length=30, default='ADMIN')

    class Meta:
        db_table = "TB_MENU_INFO"
        ordering = ['pk']

