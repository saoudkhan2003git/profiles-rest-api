from django.contrib import admin
from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello_view/', views.HelloAppView.as_view()),
]
