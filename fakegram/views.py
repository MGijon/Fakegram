""" FakeGram views """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


def hello_world(request):
	""" """
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
	return HttpResponse('Hello World, {now}'.format(now=str(now)))



def hi(request, name, age):
	return HttpResponse(name + str(age))