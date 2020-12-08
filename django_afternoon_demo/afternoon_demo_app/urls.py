from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bio', views.bio),
    path('redirect', views.redir),
    path('manyyodas/<int:val>', views.manyyodas)
]