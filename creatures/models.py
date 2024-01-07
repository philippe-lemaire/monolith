from django.db import models
from tinymce.models import HTMLField

class Creature(models.Model):
    name = models.CharField(max_length=60)
    HP = models.IntegerField()
    STR = models.IntegerField()
    DEX = models.IntegerField()
    WIL = models.IntegerField()
    armor = models.IntegerField(null=True, blank=True)
    attack1 = models.CharField(blank=True, max_length=60)
    attack2 = models.CharField(blank=True, max_length=60)
    crit = models.TextField(blank=True)
    special = HTMLField(blank=True)

    def __str__(self):
        return f"{self.name}."
