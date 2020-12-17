from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register_user', views.register_user),
    path('login_user', views.login_user),
    path('dashboard', views.dashboard),
    path('cards', views.cards),
    path('users', views.users),
    path('users/<int:id>', views.oneuser),
    path('cards/new', views.newcard),
    path('logout', views.logout),
    path('cards/add', views.add_card),
    path('collection/add/<int:id>', views.add_to_collection),
    path('collection/remove/<int:id>', views.remove_from_collection)
]