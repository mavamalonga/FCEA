from django.db import models
from authentification.models import Photo


class Club(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=200)
	photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
	presentation = models.TextField(max_length=5000)
	address = models.CharField(max_length=200)
	infrastructure = models.TextField(max_length=5000)
	secretariat = models.CharField(max_length=500)
	network_link = models.CharField(max_length=200)
	network_link_2 = models.CharField(max_length=200)

	def __str__(self):
		return self.name