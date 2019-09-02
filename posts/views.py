"""
Posts views
"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime

# Forms
from posts.forms import PostForm

posts = [
	{
		'name': 'Mont Blanck',
		'user': {
			'name': 'Fidel Castro',
			'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/a556a8d3238e6b04a40c214d114ca319/5DA0B3DB/t51.2885-19/s320x320/30841858_1277613869008038_4389283755617943552_n.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/dcde65bb3b067b2439d35640e0760173/5DBEF4EE/t51.2885-19/s320x320/41265389_2232828083617518_7336074084557520896_n.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net'
	},

	{
		'name': 'Iverest',
		'user': {
			'name': 'Gadafi',
			'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/c568d8f8d774211c72d77b55c592c203/5DB204FA/t51.2885-19/s320x320/29095601_199852094079999_986442048158564352_n.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/b609ce3c1ab280c2754751453582659e/5DADB0F3/t51.2885-19/s320x320/65421822_660524924360164_7271241188152180736_n.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net',
	},

	{
		'name': 'Monte GOrdo',
		'user': {
			'name': 'Broncano',
			'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/6f458765a0b90ab30cee7ef3a583e82f/5DB5D7F1/t51.2885-19/s320x320/51715607_1587365001366216_5742314310600753152_n.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'https://instagram.fmad8-1.fna.fbcdn.net/vp/13c182ccc26a1e3f2ad9d2b71857a79f/5DC6947E/t51.2885-19/s320x320/18011192_196797890831780_6669522665188884480_a.jpg?_nc_ht=instagram.fmad8-1.fna.fbcdn.net',
	},
]


@login_required
def list_posts(request):
	"""List existing posts."""
	return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
	"""Create new post view."""
	if request.method == 'POST':
	#	form = PostForm(request.POST, request.FILES)
	#	if form.is_valid():
	#		form.save()

	#		return redirect('feed')
		pass
	else:
		form = PostForm

	return render(
		request=request,
		template_name = 'posts/new.hml',
		context={
			'form': form, 
			'user': request.user,
			'profile': request.user.profile,
		}
	)