from django.db import models
from rest_framework import serializers

class Notification(models.Modal):
    id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length = 7)
    
    
