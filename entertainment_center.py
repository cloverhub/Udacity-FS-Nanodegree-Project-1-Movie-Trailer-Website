# This is a list of these movie objects which is used to call the constructor
# media.Movie() to instantiate movie objects.
# This list of movies is what the open_movies_page() function of
# fresh_tomatoes.py needs as input in order to build the HTML file
# to display the website.

import fresh_tomatoes
import media

# Create movie objects
jur_park = media.Movie("Jurassic Park",
                       "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                       "https://www.youtube.com/watch?v=f5C7dqrAItM")

lost_world = media.Movie("The Lost World",
                         "https://upload.wikimedia.org/wikipedia/en/c/cc/The_Lost_World_%E2%80%93_Jurassic_Park_poster.jpg",
                         "https://www.youtube.com/watch?v=vtfwgaHD5_w")

dinosaur = media.Movie("Dinosaur",
                       "https://upload.wikimedia.org/wikipedia/en/b/bc/Dinosaurmovieposter.jpg",
                       "https://www.youtube.com/watch?v=HlNRVZ871os")

were_back = media.Movie("We're Back!",
                        "https://upload.wikimedia.org/wikipedia/en/c/c6/We%27re_Back%21_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=XOLcsnqBJjI")

good_dino = media.Movie("The Good Dinosaur",
                        "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
                        "https://www.youtube.com/watch?v=O-RgquKVTPE")

land_lost = media.Movie("Land of the Lost",
                        "https://upload.wikimedia.org/wikipedia/en/9/99/Land_of_the_Lost_poster.jpg",
                        "https://www.youtube.com/watch?v=JFCDEajQwC0")

ice_age = media.Movie("Ice Age: Dawn of the Dinosaurs",
                      "https://upload.wikimedia.org/wikipedia/en/2/24/Ice_Age_Dawn_of_the_Dinosaurs_theatrical_poster.jpg",
                      "https://www.youtube.com/watch?v=Y_nSwh2WjAM")

lost_2001 = media.Movie("The Lost World (2001)",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Lost_World_%282001_film%29.jpg",
                        "https://www.youtube.com/watch?v=KXwsTDmniPM")

giants_patagonia = media.Movie("Dinosaurs: Giants of Patagonia",
                               "https://upload.wikimedia.org/wikipedia/en/f/f5/Dinosaurs_-_Giants_of_Patagonia_Poster.png",
                               "https://www.youtube.com/watch?v=OZ35NJk75bQ")

# Store each movie object in a movies list
movies = [jur_park, lost_world, dinosaur, were_back, good_dino, land_lost,
          ice_age, lost_2001, giants_patagonia]

# Use the open_movies_page function in fresh_tomatoes.py to generate the html website
fresh_tomatoes.open_movies_page(movies)
