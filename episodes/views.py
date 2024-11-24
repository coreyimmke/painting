from django.db.models import Avg, CharField, Count, Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, render
from django.views import generic

from episodes.plots.colors_per_episode_plot import colors_per_episode_plot
from episodes.plots.top_title_words_plot import top_title_words_plot

from .models import Episode


class EpisodesView(generic.ListView):
    """Creates the Episode List page."""

    model = Episode
    template_name = "episodes/episode_list.html"
    paginate_by = 13  # 13 entries per page which aligns with num episodes per season


class EpisodeDetailView(generic.DetailView):
    """Creates the Episode Detail pages."""

    model = Episode
    template_name = "episodes/episode_detail.html"

    def get_object(self, queryset=None):
        """Explicity set how to query for the episode for the applicable page."""
        return get_object_or_404(
            Episode,
            season_number=self.kwargs.get("season"),
            episode_number=self.kwargs.get("episode"),
        )


def home(request):
    """Creates the home page view."""

    # Pull all the episodes along with their count of the number of colors they use
    # and a string of the season and episode to be used for distinguishing episodes
    # in the colors per episode plot
    episodes = Episode.objects.all().annotate(
        color_count=Count("colors"),
        season_episode=Concat(
            Value("Season "),
            "season_number",
            Value(" Episode "),
            "episode_number",
            output_field=CharField(),
        ),
    )
    episode_count = episodes.count()
    avg_number_colors = episodes.aggregate(avg_colors=Avg("color_count"))["avg_colors"]

    colors_per_episode_plot_div = colors_per_episode_plot(episodes)
    top_title_words_plot_div = top_title_words_plot(episodes)

    return render(
        request,
        template_name="episodes/home.html",
        context={
            "episode_count": episode_count,
            "avg_colors": avg_number_colors,
            "colors_per_episode_plot": colors_per_episode_plot_div,
            "top_title_words_plot": top_title_words_plot_div,
        },
    )
