from django.urls import path

from . import views

app_name = "chargen"

urlpatterns = [
    path("", views.generate_character, name="generate_character"),
]
