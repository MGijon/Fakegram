"""Posts models."""

# Django 
from django.db import models

class User(models.Model):
	"""User model."""
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)  

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	is_admin = models.BooleanField(default = False)

	bio = models.TextField()

	birthdate = models.DateField(blank=True, null=True) # we allow non added and the deefault value is now

	created = models.DateTimeField(auto_now_add=True) # filled when created
	modified = models.DateTimeField(auto_now=True)  # filled when opened  