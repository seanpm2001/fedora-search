from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=100)
    summary = models.TextField()
    description = models.TextField()
    point_of_contact = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    upstream_url = models.CharField(max_length=100)
