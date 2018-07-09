from django.db import models
from rest_framework import serializers
# Create your models here.

class Coin(models.Model):
    id = models.AutoField(primary_key=True)
    coin_name = models.CharField(max_length=20)
    
class Session(models.Model):
    email = models.CharField(max_length=20, default='') 
    phone = models.IntegerField(default='')
    
class Noftification(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    volume_delta = models.FloatField()
    price_delta = models.FloatField()
    
class Ticker(models.Model):
    volume = models.FloatField() 
    price = models.FloatField()
    market_cap = models.IntegerField()
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    
#this is the serializer for the contact model, it explains what fields should be included into the json
class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id','coin_name', 'market_cap', 'volume', 'price', 'email', 'phone', 'coin', 'session', 'volume_delta', 'price_delta')
# Create your models here.
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'email', 'phone')
# Create your models here.
