"""Post forms."""

# Django
from djnago import forms

# Models
from post.models import Post

class PostForm(forms.ModelForm):
	"""Post model form."""

	class Meta:
		"""Form settins."""

		model = Post 
		fields = ('user', 'profile', 'title', 'photo')