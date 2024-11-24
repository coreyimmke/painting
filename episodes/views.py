from django.views import generic

from .models import Episode


class EpisodesView(generic.ListView):
    model = Episode
    template_name = "episodes/episode_list.html"
    paginate_by = 13  # 13 entries per page which aligns with num episodes per season
