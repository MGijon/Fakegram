"""User admin classes."""

# Django
from django.contrib import admin

# Models 
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