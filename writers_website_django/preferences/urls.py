from django.urls import path

from . import views

app_name = 'user_preferences'
urlpatterns = [
 path('', views.edit, name='edit'),
 path('edit/<int:preferences_id>/', views.edit, name='edit')
]