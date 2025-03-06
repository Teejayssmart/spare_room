from django.urls import path

from . import views

urlpatterns = [
    path("single_rooms", views.single_rooms)
]

urlpatterns = [
    path("double_rooms", views.double_rooms)
]
