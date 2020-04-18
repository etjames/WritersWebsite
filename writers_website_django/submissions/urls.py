from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:submission_id>/', views.detail, name='detail'),
]