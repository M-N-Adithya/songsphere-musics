from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path("", views.key, name="key"),
]