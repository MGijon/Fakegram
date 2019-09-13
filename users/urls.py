"""Users URLs."""

# Django 
from django.urls import path 

# Views
from users import views


## DJANGO RESUELVE LAS URLs EN EL ORDEN QUE LAS PONGAMOS


urlpatterns =[

	# Management
	path(
		route = 'users/login/', 
		view = views.login_view, 
		name ='login'
	),

    path(
    	route = 'users/logout/', 
    	view = views.logout_view, 
    	name ='logout'
    ),

    path(
    	route = 'users/signup/', 
    	view = views.SignupView.as_view(),
    	name ='signup'
    ),

    path(
    	route = 'users/me/profile/', 
    	view = views.update_profile, 
    	name = 'update_profile'
	),

    # Posts
    path(
        route = '<str:username>/',
        view = views.UserDetailView.as_view(),
        name = 'detail'
    ),
]