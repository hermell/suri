from django.db import models
from django.utils import timezone

class Menu(models.Model):

    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=30)
    level = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.DecimalField(max_digits=10, decimal_places=2)
    up_menu_id = models.CharField(max_length=5)
    register_date = models.DateTimeField(default=timezone.now)
    register_id = models.DecimalField(max_digits=11, decimal_places=2)
    update_date = models.DateTimeField(default=timezone.now)
    update_id = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = "TB_MENU_INFO"