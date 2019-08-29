"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models 
from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	"""Profile admin."""

	# se mostrarán los siguientes campos en el panel de administración sobre cada usuario
	list_display = (
		'pk', 
		'user', 
		'phone_number', 
		'website', 
		'picture',
	)

	# campos sobre los que al pulsar nos lleven al detalle de cada perfil
	list_display_links = (
		'pk', 
		'user', 
		'phone_number',
	)

	# campos editables con un click
	list_editable = (
		'picture',
	) 

	# campos por los que podremos buscar en los perfiles
	search_fields = (
		'user__email', 
		'user__first_name', 
		'user__last_name', 
		'phone_number',
	) 

	# campos a los que podemos aplicarles filtros
	list_filter = (
		'user__is_active',
		'user__is_staff',
	)

	fieldsets = (
		('Profile', {
			'fields': (
				('user', 'picture'),),
			}),
		('Extra info', {
			'fields': (
				('website', 'phone_number'),
				('biography'),),
			}),
		#('Metadata', {
		#	'fields': (('created', 'modified'),),
		#	}),
	)

	#readonly_fields = ('created', 'modified',)

class ProfileInLine(admin.StackedInline):
	"""Profile in-line admin for users."""

	model = Profile
	can_delete = False
	verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
	"""Add profile admin to base user admin."""
	inlines = (ProfileInLine,) # es una tupla
	list_display = (
		'username',
		'email',
		'first_name',
		'last_name',
		'is_active',
		'is_staff',
	)

# tenemos que desregistrar el que ya existía y registrar el nuevo
admin.site.unregister(User)
admin.site.register(User, UserAdmin) # recibe el modelo y también la clase que vamos a utilizar
