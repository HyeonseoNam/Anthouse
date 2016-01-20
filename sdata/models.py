from django.conf import settings
from django.db import models


class Stock(models.Model):
    s_name = models.CharField(max_length=20)
    s_code = models.CharField(max_length=10)
    s_open = models.CharField(max_length=20, null=True)
    s_close = models.CharField(max_length=20, null=True)
    s_date = models.CharField(max_length=20, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.s_name
