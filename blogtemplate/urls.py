from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:blog_id>/', views.blog_details, name = 'blog_details'),
	path('new/', views.blog_new, name='blog_new'),
	path('<int:blog_id>/edit', views.blog_edit, name = 'blog_edit'),
	path('<int:blog_id>/delete', views.blog_delete, name = 'blog_delete'),
]