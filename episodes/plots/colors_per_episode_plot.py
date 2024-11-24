import plotly.graph_objects as go
from plotly.offline import plot


def colors_per_episode_plot(episodes):
    """
    Creates the colors per episode plot.

    Args:
        episodes: QuerySet of episodes data

    Returns:
        A plotly scatter plot showing number of colors used for each episode
    """
    x_values = [
        episode for episode in episodes.values_list("season_episode", flat=True)
    ]
    y_values = [count for count in episodes.values_list("color_count", flat=True)]

    line_plot = go.Figure(
        data=[
            go.Scatter(
                x=x_values,
                y=y_values,
            )
        ]
    )
    line_plot.update_xaxes(
        ticktext=[f"Season {i}" for i in range(1, len(x_values) + 1)],
        tickvals=[f"Season {i} Episode 1" for i in range(1, len(x_values) + 1)],
    )
    line_plot.update_yaxes(title_text="Number of Colors Used")
    line_plot.update_layout(
        title={
            "text": "Number of Colors Used For Each Episode",
            "font": {
                "size": 20,
            },
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        }
    )

    return plot(line_plot, output_type="div")
