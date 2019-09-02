"""Users views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User 
from users.models import Profile

# Exception
from django.db.utils import IntegrityError 

# Forms
from users.forms import ProfileForm

def login_view(request):
	"""Login view."""
	if request.method == 'POST':
	
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('feed') # nombre que le hemos dado a la url en urls.py, así si cambia la url sigue funcionando
		else:
			return render(request, 'users/login.html', {'error': 'Invalid username and password'})
	return render(request, 'users/login.html')



def signup(request):
	"""Sign up view."""
	if request.method == 'POST':

		username = request.POST['username']
		passw = request.POST['password']
		passw_confirmation = request.POST['password_confirmation']

		if passw != passw_confirmation:
			return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

		try:
			user = User.objects.create_user(username=username, password=passw) # en este punto el usuario ya está guardado en la db
		except IntegrityError:
			return render(request, 'users/signup.html', {'error': 'Username is already in user'})

		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']

		# ahora guardamos los datos en la db creando una instancia de la clase Profile
		profile = Profile(user=user)
		profile.save()

		return redirect('login')

	return render(request, 'users/signup.html')


@login_required
def logout_view(request):
	"""Logout view."""
	logout(request)
	return redirect('login')

@login_required
def update_profile(request):
	"""Update a user's profile view."""
	profile = request.user.profile
	
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES) # post para los caracteres y files para la foto

		if form.is_valid():
			data = form.cleaned_data

			profile.website = data['website']
			profile.biography = data['biography']
			profile.phone_number = data['phone_number']
			profile.picture = data['picture']
			profile.save()

			return redirect('update_profile')
	else:
		form = ProfileForm()

	return render(
		request=request, 
		template_name='users/update_profile.html',
		context={
			'profile': profile,
			'user': request.user,
			'form': form,
		}
	) 
