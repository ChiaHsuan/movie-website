import media
import fresh_tomatoes
import csv
# Create media.Movie Instances
# Movie arguments: title, cover_image_url, introduction, youtube_trailer_url
# Load CSV data

zootopia = media.Movie(
		"Zootopia",
		"img/zootopia.jpg", #image url
		"Rabbits!!", # introduction
		"https://www.youtube.com/watch?v=jWM0ct-OLsM" # youtube trailer
		)

imitation_game = media.Movie(
		"Imitation Game", 
		"http://i.telegraph.co.uk/multimedia/archive/03092/SHOT_11_029__3092453b.jpg", 
		"Rabbits!!", 
		"https://www.youtube.com/watch?v=jWM0ct-OLsM")

lord_of_rings = media.Movie(
		"Lord of the Rings", 
		"https://images8.alphacoders.com/462/462581.jpg", 
		"Rabbits!!", 
		"https://www.youtube.com/watch?v=jWM0ct-OLsM")

# create a movie array
myMovies = [ zootopia, imitation_game, lord_of_rings ];

# open the movie website page
fresh_tomatoes.open_movies_page(myMovies)
