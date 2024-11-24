from collections import Counter

import plotly.graph_objects as go
from plotly.offline import plot


def get_count_of_title_words(episodes):
    """
    Gets a count of how many times a word is used in a title

    Excludes common articles and prepositions.

    Args:
        episodes: QuerySet of episodes data

    Returns:
        A Counter with a count of each time a word is used
    """
    articles_and_prepositions = ["a", "an", "in", "at", "the", "of", "to"]
    title_words = [
        word
        for title in episodes.values_list("painting_title", flat=True)
        for word in title.lower().split()
        if word not in articles_and_prepositions
    ]
    return Counter(title_words)


def top_title_words_plot(episodes):
    """
    Creates the top title words plot.

    Shows the top 20 words (excludes common articles and prepositions)

    Args:
        episodes: QuerySet of episodes data

    Returns:
        A plotly bar plot showing how many times a word is used in a painting title
    """
    word_counts = get_count_of_title_words(episodes)

    # Build x and y values from the 20 most common title words
    x_values = []
    y_values = []
    for word, count in word_counts.most_common(20):
        x_values.append(word)
        y_values.append(count)

    bar_plot = go.Figure(
        data=[
            go.Bar(
                x=x_values,
                y=y_values,
            )
        ]
    )
    bar_plot.update_yaxes(title_text="Number of Paintings")
    bar_plot.update_layout(
        title={
            "text": "Number of Paintings Word Appeared in Title",
            "font": {
                "size": 20,
            },
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        }
    )

    return plot(bar_plot, output_type="div")
