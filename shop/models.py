from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=300)
	price = models.DecimalField(max_digits=6,decimal_places=2)
	description = models.TextField()
	image = models.ImageField()
	likes = models.IntegerField()

	def __str__(self):

		return str(self.name)

class Review(models.Model):
	rewiews = models.TextField()
	item = models.ForeignKey(Item)


