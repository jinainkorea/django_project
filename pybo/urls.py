from django.contrib import admin
from django.urls import path, include

from pybo import views

urlpatterns = [
    path('', views.index),
    path('question', views.index2),]
