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


class Event(models.Model):

	title = models.CharField(max_length=50)
	description = models.TextField(max_length=8192)
	date = models.DateTimeField()
	address = models.CharField(max_length=200)
	photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name


class Category(models.Model):
    Biberon = 'Biberon (U7) : 5 ans et 6 ans'
    Debutant = 'Debutant (U8, U9) : 7 ans, 8 ans'
    Poussin = 'Poussin (U10, U11) : de 9 à 10 ans'
    Benjamin = 'Benjamin (U12, U13) : de 11 à 12 ans'
    Minime = 'Minime (U14, U15) : de 13 à 14 ans'
    Cadet = 'Cadet (U16, U17) : de 15 à 16 ans'
    Junior = 'Junior (U18, U19) : de 17 à 18 ans'
    Espoir = 'Espoir (U19, U20) : de 18 à 20 ans'
    Senior = 'Senior'
    Veteran = 'Veteran au-delà de 35 ans'
    CDM = 'CDM'
    CATEGORY_CHOICES = [
        (Biberon, 'Biberon'),
        (Debutant, 'Debutant'),
        (Poussin, 'Poussin'),
        (Benjamin, 'Benjamin'),
        (Minime, 'Minime'),
        (Cadet, 'Cadet'),
        (Junior, 'Junior'),
        (Espoir, 'Espoir'),
        (Senior, 'Senior'),
        (Veteran, 'Veteran'),
        (CDM, 'CDM'),
    ]
    category_choices = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=Biberon,
    )

    def __str__(self):
        return self.category_choices


class Level(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    LEVEL_CHOICES = [
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
        (E, 'E'),
    ]
    level_choice = models.CharField(
        max_length=2,
        choices=LEVEL_CHOICES,
        default=A,
    )

    def __str__(self):
        return self.level_choice


class Team(models.Model):
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
	coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='coach')
	coach_adj = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
		related_name='adjoint')
	photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
	classement = models.CharField(max_length=20, null=True)
	agenda = models.CharField(max_length=20, null=True)

	def __str__(self):
		return str(self.category)

	def __str__(self):
		return self.name