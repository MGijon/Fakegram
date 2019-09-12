"""Users views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse

# Models 
from django.contrib.auth.models import User
from posts.models import Posts

# Forms
from users.forms import ProfileForm, SignupForm

def login_view(request):
	"""Login view."""
	if request.method == 'POST':
	
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('posts:feed') # nombre que le hemos dado a la url en urls.py, así si cambia la url sigue funcionando
		else:
			return render(request, 'users/login.html', {'error': 'Invalid username and password'})
	return render(request, 'users/login.html')



def signup(request):
	"""Sign up view."""
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('users:login')
	else:
		form = SignupForm()

	return render(
		request=request,
		template_name='users/signup.html', 
		context={
			'form': form
		}
	)


		
@login_required
def logout_view(request):
	"""Logout view."""
	logout(request)
	return redirect('users:login')

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

			url = reverse('users:detail', kwargs={'username': request.user.username})
			return redirect(url)
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


class UserDetailView(LoginRequiredMixin, DetailView):
	"""User detail view."""

	template_name = 'users/detail.html'	
	slug_field = 'username'
	slug_url_kwarg = 'username' # aqiñi va el término que hemos usado para llamar al string en las urls
	queryset = User.objects.all()

	context_object_name = 'user'

	def get_context_data(self, **kwargs):
		"""Add user's posts to context."""
		context = super().get_context_data(**kwargs)
		user = self.get_object()
		context['posts'] = Posts.objects.filter(user=user).order_by('-created')
		return context

