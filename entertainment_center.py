import fresh_tomatoes
import media

jurassic_park = media.Movie("Jurassic Park",
                        "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",
                        "https://www.youtube.com/watch?v=f5C7dqrAItM")

the_lost_world = media.Movie("The Lost World",
                        "https://upload.wikimedia.org/wikipedia/en/c/cc/The_Lost_World_%E2%80%93_Jurassic_Park_poster.jpg",
                        "https://www.youtube.com/watch?v=vtfwgaHD5_w")

dinosaur = media.Movie("Dinosaur",
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Dinosaurmovieposter.jpg",
                        "https://www.youtube.com/watch?v=HlNRVZ871os")

were_back = media.Movie("We're Back!",
                        "https://upload.wikimedia.org/wikipedia/en/c/c6/We%27re_Back%21_Movie_Poster.jpg",
                        "https://www.youtube.com/watch?v=XOLcsnqBJjI")

the_good_dinosaur = media.Movie("The Good Dinosaur",
                        "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
                        "https://www.youtube.com/watch?v=O-RgquKVTPE")


land_of_the_lost = media.Movie("Land of the Lost",
                        "https://upload.wikimedia.org/wikipedia/en/9/99/Land_of_the_Lost_poster.jpg",
                        "https://www.youtube.com/watch?v=JFCDEajQwC0")

ice_age_dawn_of_the_dinosaurs = media.Movie("Ice Age: Dawn of the Dinosaurs",
                        "https://upload.wikimedia.org/wikipedia/en/2/24/Ice_Age_Dawn_of_the_Dinosaurs_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=Y_nSwh2WjAM")

the_lost_world_2001 = media.Movie("The Lost World (2001)",
                        "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Lost_World_%282001_film%29.jpg",
                        "https://www.youtube.com/watch?v=KXwsTDmniPM")

dinosaurs_giants_of_patagonia = media.Movie("Dinosaurs: Giants of Patagonia",
                        "https://upload.wikimedia.org/wikipedia/en/f/f5/Dinosaurs_-_Giants_of_Patagonia_Poster.png",
                        "https://www.youtube.com/watch?v=OZ35NJk75bQ")

movies = [jurassic_park, the_lost_world, dinosaur, were_back, the_good_dinosaur, land_of_the_lost, ice_age_dawn_of_the_dinosaurs, the_lost_world_2001, dinosaurs_giants_of_patagonia]
fresh_tomatoes.open_movies_page(movies)
