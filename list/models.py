from django.db import models
from django.utils import timezone


# Create your models here.
class school(models.Model):
    name = models.CharField(max_length=50)
    system = models.CharField(max_length=50)

    def __str__(self):
        return self.system + ":" + self.name


class tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class spell(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, default="none")
    castingtime = models.CharField(max_length=50, default="standard")
    range = models.CharField(max_length=20, default="self")
    duration = models.CharField(max_length=50, default="none")
    cooldown = models.CharField(max_length=50, default="none")
    resource = models.CharField(max_length=50, default="0")
    component = models.TextField(blank=True)
    materials = models.TextField(blank=True)
    description = models.TextField(default="")
    schools = models.ManyToManyField(school)
    tags = models.ManyToManyField(tag, blank=True)

    def __str__(self):
        return self.name
