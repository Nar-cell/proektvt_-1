from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
]
