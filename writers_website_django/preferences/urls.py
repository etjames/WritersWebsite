from django.urls import path

from . import views

app_name = 'preferences'
urlpatterns = [
 path('', views.edit),
 path('edit/<int:preferences_id>/', views.edit, name='edit')
]