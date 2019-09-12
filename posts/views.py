"""
Posts views
"""

# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Utilities
from datetime import datetime # useless now

# Forms
from posts.forms import PostForm

# Models
from posts.models import Posts


#@login_required
#def list_posts(request):
#	"""List existing posts."""
#	posts = Posts.objects.all().order_by('-created')
#	return render(request, 'posts/feed.html', {'posts': posts})

class PostsFeedView(LoginRequiredMixin, ListView):
	"""Return all published posts."""

	template_name = 'posts/feed.html'
	model = Posts 
	ordering = ('-created',)
	paginate_by = 2 # number of elements by page
	context_object_name = 'posts'

@login_required
def create_post(request):
	"""Create new post view."""
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return redirect('posts:feed')
		pass
	else:
		form = PostForm

	return render(
		request=request,
		template_name = 'posts/new.html',
		context={
			'form': form, 
			'user': request.user,
			'profile': request.user.profile,
		}
	)