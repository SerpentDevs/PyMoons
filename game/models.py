from django.db import models


# Create your models here.
class Acs(models.Model):
    name = models.CharField(max_length=50, null=True, default=None)
    target = models.PositiveIntegerField()
    arrival = models.IntegerField(null=True, default=None)


class Alliance(models.Model):
    ally_name = models.CharField(max_length=50, default='')
    ally_tag = models.CharField(max_length=20, default='')
    ally_owner = models.PositiveIntegerField(default=0)
    ally_register_time = models.IntegerField(default=0)
    ally_description = models.TextField()
    ally_web = models.CharField(max_length=255, default='')
