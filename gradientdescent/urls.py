from django.urls import path

from . import views

app_name = "gradientdescent"

urlpatterns = [
    path("encounters", views.roll_encounters_view, name="roll_encounters"),
]
