from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('short/<str:url>/', views.match, name='match_url'),
]