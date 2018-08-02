# This file creates a movie class to define properties of a movie used by
# the open_movies_page() function of fresh_tomatoes.py

import webbrowser


class Movie():
    """ This class provides a way to store movie related information.

    Attributes:
        title (str): The title of the movie.
        poster_image_url (str): A URL to the box art image for the movie.
        trailer_youtube_url (str): A URL to the youTube trailer for the movie.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ this contructor initializes values for the Movie class."""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Uses webbrowser to show the movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
