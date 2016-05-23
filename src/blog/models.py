from __future__ import unicode_literals

from django.db import models

class Account(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email	 = models.EmailField(max_length=200)
	created  = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username