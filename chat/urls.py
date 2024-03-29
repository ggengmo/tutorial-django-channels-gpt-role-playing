from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.role_playing_room_list, name="role_playing_room_list"),
    path("<int:pk>/", views.role_playing_room_detail, name="role_playing_room_detail"),
    path('new/', views.role_playing_room_new, name="role_playing_room_new"),
    path("<int:pk>/edit/", views.role_playing_room_edit, name="role_playing_room_edit"),
    path("<int:pk>/delete/", views.role_playing_room_delete, name="role_playing_room_delete"),
]