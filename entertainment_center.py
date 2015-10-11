# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

bull_durham = media.Movie("Bull Durham",
                          "A witty blend of sports drama, intelligent comedy \
                          and sexy romance Bull Durham is an ideal date film.",
                          "https://upload.wikimedia.org/wikipedia/en/e/ef/Bull_Durham_film_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=dnJFndf-Krg",
                          "Kevin Costner, Susan Sarandon",
                          "(1988)")

moneyball = media.Movie("Moneyball",
                        "Based on a true story, Moneyball is a movie for \
                        anybody who has ever dreamed of taking on the system.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",   # noqa
                        "https://www.youtube.com/watch?v=BwIBZi1RcNI",
                        "Brad Pitt, Jonah Hill",
                        "(2011)")

badnews_bears = media.Movie("Bad News Bears",
                            "The success of this underdog comedy from director\
                            Michael Ritchie almost single-handedly spawned \
                            the kids' sports film boom of the 1980s and 90s.",
                            "https://upload.wikimedia.org/wikipedia/en/f/f9/Bad_news_bears_1976_movie_poster.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sF6De-XP7x4",
                            "Walter Matthau, Tatum O'Neal",
                            "(1976)")

bangthe_drumslowly = media.Movie("Bang the Drum Slowly",
                                 "Bang the Drum Slowly is a touching melodrama \
                                 that explores the inner workings of a \
                                 baseball club and its players' personalities \
                                 with remarkable depth.",
                                 "https://upload.wikimedia.org/wikipedia/en/0/0e/Bang_the_Drum_Slowly_poster.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=Xa3EdS3l1zs",
                                 "Michael Moriarity, Robert DeNiro",
                                 "(1973)")

aleague_oftheirown = media.Movie("A League of Their Own",
                                 "Sentimental and light, but still thoroughly \
                                 charming, 'A League of Their Own' is buoyed \
                                 by solid performances from a wonderful cast.",
                                 "https://upload.wikimedia.org/wikipedia/en/5/5f/League_of_their_own_ver2.jpg",  # noqa
                                 "https://www.youtube.com/watch?v=WcN392H2jx0",
                                 "Tom Hanks, Geena Davis, Madonna",
                                 "(1992)")

eightmen_out = media.Movie("Eight Men Out",
                           "Basing his screenplay on a notorious moment in \
                           the history of American baseball, writer/director \
                           John Sayles offers an insightful look into the \
                           great Black Sox scandal of 1919.",
                           "https://upload.wikimedia.org/wikipedia/en/4/41/Eight_Men_Out_DVD_cover.jpg",   # noqa
                           "https://www.youtube.com/watch?v=JSHQw85pvek",
                           "John Cusack, Charlie Sheen",
                           "(1988)")

movies = [bull_durham, moneyball, badnews_bears, bangthe_drumslowly,
          aleague_oftheirown, eightmen_out]
fresh_tomatoes.open_movies_page(movies)
