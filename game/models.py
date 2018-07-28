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
    ally_text = models.TextField()
    ally_image = models.CharField(max_length=255, default='')
    ally_request = models.CharField(max_length=1000, null=True, default=None)
    ally_request_notallow = models.BooleanField(default=False)
    ally_request_min_points = models.PositiveIntegerField(default=0)
    ally_owner_range = models.CharField(max_length=32)
    ally_members = models.PositiveSmallIntegerField()
    ally_stats = models.BooleanField(default=True)
    ally_diplo = models.BooleanField(default=True)
    ally_universe = models.PositiveSmallIntegerField()
    ally_max_members = models.PositiveIntegerField(default=20)
    ally_events = models.CharField(max_length=55, default='')


class AllianceRanks(models.Model):
    rank_name = models.CharField(max_length=32)
    alliance_id = models.PositiveIntegerField()
    member_list = models.PositiveSmallIntegerField(default=0)
    online_state = models.PositiveSmallIntegerField(default=0)
    transfer = models.PositiveSmallIntegerField(default=0)
    see_apply = models.PositiveSmallIntegerField(default=0)
    manage_apply = models.PositiveSmallIntegerField(default=0)
    round_mail = models.PositiveSmallIntegerField(default=0)
    admin = models.PositiveSmallIntegerField(default=0)
    kick = models.PositiveSmallIntegerField(default=0)
    diplomatic = models.PositiveSmallIntegerField(default=0)
    ranks = models.PositiveSmallIntegerField(default=0)
    manage_users = models.PositiveSmallIntegerField(default=0)
    events = models.PositiveSmallIntegerField(default=0)


 class AllianceRequest(models.Model):
     text = models.TextField()
     user_id = models.PositiveIntegerField()
     alliance_id = models.PositiveIntegerField()
     time = models.IntegerField()