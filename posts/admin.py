"""Posts admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models 
from django.contrib.auth.models import User
from posts.models import Posts

# Register your models here.

@admin.register(Posts)
class ProfileAdmin(admin.ModelAdmin):
	"""Posts admin."""



class ProfileInLine(admin.StackedInline):
	"""Profile in-line admin for users."""

	model = Posts
	can_delete = False
	verbose_name_plural = 'profiles'
