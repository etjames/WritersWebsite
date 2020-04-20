from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
	path('', views.list, name='list'),
	path('new/', views.matches, name='matches'),
	path('new/<int:submission_id>/', views.new, name='new'),
	path('edit/<int:review_id>/', views.edit, name='edit')
]