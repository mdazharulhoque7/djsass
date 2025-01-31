from django.db import models

# Create your models here.

class PageVisit(models.Model):
    path = models.CharField(blank=True, null=True, max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)