#  Re-run PEP-8 guidelines http://pep8online.com/

# File forked from Udacity Github that provides HTML,
# styling, scripting, and functions
import fresh_tomatoes

# The Movie class definition
import media

# The title, theme, poster, and trailer are listed for each movie
# The code "  # NOQA" added to each long URL to prevent linter warnings
princess_bride = media.Movie("Princess Bride",
                             "A fairy tale adventure about a beautiful young"
                             " woman and her one true love.",
                             "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                             "https://www.youtube.com/watch?v=njZBYfNpWoE  # NOQA")

terminator = media.Movie("Terminator",
                         "Disguised as a human, a cyborg assassin known as a"
                         " Terminator travels from 2029 to 1984 to kill Sarah"
                         " Connor.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Terminator1984movieposter.jpg/220px-Terminator1984movieposter.jpg",
                         "https://www.youtube.com/watch?v=c4Jo8QoOTQ4  # NOQA")

big_fish = media.Movie("Big Fish",
                       "A father's quest to be a big fish in a big pond,"
                       " and the son's quest to see through his tall"
                       " tales.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Big_Fish_movie_poster.png/220px-Big_Fish_movie_poster.png",
                       "https://www.youtube.com/watch?v=M3YVTgTl-F0  # NOQA")

lord_of_the_rings = media.Movie("Lord of The Rings",
                                "The future of civilization rests in the fate of"
                                " the One Ring",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4  # NOQA")

matrix = media.Movie("Matrix",
                     "You may be The One",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/06/Ultimate_Matrix_Collection_poster.jpg/220px-Ultimate_Matrix_Collection_poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU  # NOQA")

so_i_married_an_axe_murderer = media.Movie("So I Married An Axe Murderer",
                                           "The Honeymoon was Killer",
                                           "https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/Axemurderermovieposter.jpg/220px-Axemurderermovieposter.jpg",
                                           "https://www.youtube.com/watch?v=O3TgDBN7wk4  # NOQA")

# Create variable to send to open_movies_page in fresh_tomatoes
movies = [princess_bride, terminator, big_fish, lord_of_the_rings, matrix, so_i_married_an_axe_murderer]

# Call the function to open the movie page URL with the listed movies
fresh_tomatoes.open_movies_page(movies)
