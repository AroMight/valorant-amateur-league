from django.urls import path
from . import views

app_name = "players"

urlpatterns = [
    path("logout/", views.PlayerLogoutView.as_view(), name="logout"),
]
