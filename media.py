# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

# This class provides a way to store movie related information


class Movie():
    """This class provides a way to store movie related information including\
    title, storyline, poster image, online trailer video, list of the stars \
    and the release year. """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_stars, release_year):
        """ This is the constructor method which instantiates each movie with \
        data provided in other functions """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.stars = movie_stars
        self.release_year = release_year

    def show_trailer(self):
        """ This function launches the trailer with the video contained \
        in the trailer_youtube_url variable."""
        webbrowser.open(self.trailer_youtube_url)
