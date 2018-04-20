from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apiindex'),
	path('<int:blog_id>/', views.blog_details, name = 'apiblog_details'),
	path('add/', views.index, name = 'apiindex')
]