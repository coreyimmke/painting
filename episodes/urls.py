from django.urls import path

from . import views

urlpatterns = [
    path("episodes/", views.EpisodesView.as_view(), name="episodes"),
]
