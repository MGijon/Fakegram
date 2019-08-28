"""Posts models.:
   It is not usefull since we are going to use the Django auth_user model for the Fakegram app.
"""

# Django 
from django.db import models

class User(models.Model):
	"""User model."""
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)  

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	country = models.CharField(max_length=100, default=False)
	city = models.CharField(max_length=100, default=False)

	is_admin = models.BooleanField(default = False)

	bio = models.TextField(blank=True)   

	birthdate = models.DateField(blank=True, null=True) # we allow non added and the deefault value is now

	created = models.DateTimeField(auto_now_add=True) # filled when created
	modified = models.DateTimeField(auto_now=True)  # filled when opened  

''' Fake data generated with instructional purpose:
users = [
	{
		email = 'andromeda@gmail.com',
		password = '1234567',
		first_name = 'andromeda',
		last_name = 'gonzales',
		city = 'Barcelona',
		country = 'Spain',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
	{
		email = '',
		password = '',
		first_name = '',
		last_name = '',
	},
]
'''