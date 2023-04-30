from django.urls import path
from barkevichdjango import views

urlpatterns = [
    path('', views.index),
    path('about', views.about)
]
