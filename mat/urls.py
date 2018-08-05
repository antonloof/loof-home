from django.urls import path

import mat.views as views 

urlpatterns = [
	path('', views.index, name='index'),
]