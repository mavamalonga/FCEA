from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator


class User(AbstractUser, models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
		message="Phone number must be entered in the format: '+999999999'")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)

	def __str__(self):
		return self.first_name

class Photo(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField()
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name