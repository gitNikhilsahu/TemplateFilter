from django.db import models

class FilterModel(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    date = models.DateField()