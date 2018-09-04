from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkin, name='index'),
    path('overview/', views.overview, name='overview'),
    path('checkin/', views.checkin, name='checkin')
]