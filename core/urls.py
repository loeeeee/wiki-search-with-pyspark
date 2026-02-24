"""
URL configuration for the core application.
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
