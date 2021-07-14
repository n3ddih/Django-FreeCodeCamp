from django.urls import path
from . import views 

urlpatterns = [
	path('', views.static, name='static'),
	# path('<str:s>', views.static, name='static'),
	path('counter', views.counter, name='counter'),
	path('index', views.index, name='index'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
	path('register', views.register, name='register'),
	path('post/<str:post_id>', views.post, name='post'),
]