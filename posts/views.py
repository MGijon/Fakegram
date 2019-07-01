"""
Posts views 
"""

# Django
from django.shortcuts import render
from django.http import HttpResponse

# Utilities
from datetime import datetime


posts = [
	{
		'name': 'Mont Blanck',
		'user': 'Fidel Castro',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'urlaquideunaimagenchulamuhahahahahhaha'
	},
	{
		'name': 'Iverest',
		'user': 'Gadafi',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'urlaquideunaimagenchulamuhahahahahhaha'
	},
	{
		'name': 'Monte GOrdo',
		'user': 'Broncano',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'picture': 'urlaquideunaimagenchulamuhahahahahhaha'
	},
]



def list_posts(request):
	"""List existing posts."""

	content = []
	for post in posts:
		content.append(""" 
			<p><strong>{name}</strong></p>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}" /></figure>
		""".format(**post)
		)
	return HttpResponse('<br>'.join(content))

	