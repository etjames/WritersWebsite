from django.urls import path

from . import views

app_name = 'submissions'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:submission_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('edit/<int:submission_id>/', views.edit, name='edit')
]