from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkin, name='index'),
    path('overview/', views.overview, name='overview'),
    path('checkin/', views.checkin, name='checkin'),
    path('bartest/', views.bartest, name='bartest'),
    path('export/', views.export, name='export'),
    # path('reset/', views.reset_db, name='reset'),
    path('summary/', views.summary, name='summary'),
    path('bartest/<int:num_selection>/', views.bartest, name='bartest'),
]