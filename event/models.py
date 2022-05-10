from django.db import models
from authentification.models import User, Photo


class Event(models.Model):

	title = models.CharField(max_length=50)
	description = models.TextField(max_length=8192)
	date = models.DateTimeField()
	address = models.CharField(max_length=200)
	photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name