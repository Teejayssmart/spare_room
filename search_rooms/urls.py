from django.urls import path

from . import views

urlpatterns = [
    path("<int:rooms>", views.just_rooms_by_number),
    path("<str:rooms>", views.just_rooms)
]
