from django.db import models,players


class players(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    
