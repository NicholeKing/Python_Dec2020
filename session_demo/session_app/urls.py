from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('play', views.play),
    path('sleep', views.sleep),
    path('feed', views.feed),
    path('work', views.work),
    path('reset', views.reset)
]