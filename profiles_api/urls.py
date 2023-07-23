from django.contrib import admin
from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
urlpatterns = [
    path('hello-view/', views.HelloAppView.as_view()),
    path('',include(router.urls))
]
