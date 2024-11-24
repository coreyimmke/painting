from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Episode


class EpisodesView(generic.ListView):
    model = Episode
    template_name = "episodes/episode_list.html"
    paginate_by = 13  # 13 entries per page which aligns with num episodes per season


class EpisodeDetailView(generic.DetailView):
    model = Episode
    template_name = "episodes/episode_detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Episode,
            season_number=self.kwargs.get("season"),
            episode_number=self.kwargs.get("episode"),
        )
