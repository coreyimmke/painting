from django.urls import path

from . import views

urlpatterns = [
    path("episodes/", views.EpisodesView.as_view(), name="episode_list"),
    path(
        "season/<int:season>/episode/<int:episode>/",
        views.EpisodeDetailView.as_view(),
        name="episode_detail",
    ),
]
