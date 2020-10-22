from django.db import models
# Create your models here.

class Rumble(models.Model):
	# id = models.IntegerField(primary_key=True)
	ip = models.CharField(max_length=200, default='0.0.0.0/0')
	port = models.IntegerField(default=80)
	alive = models.CharField(max_length=25, default=False)
	addresses = models.CharField(max_length=200, default='0.0.0.0/0')
	addresses_extra = models.CharField(max_length=200, default='0.0.0.0/0')

