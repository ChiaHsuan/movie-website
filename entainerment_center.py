import media
import fresh_tomatoes
import csv

# Define a function that read myMovie.csv 
# and create Movie instance from the csv file
def get_movie_list(file_name):
	
	# Initialize a list for storing movie data
	movie_list = []
	
	# Read file.csv and create media.Movie Instances
	with open(file_name, 'rt') as movie_csv:
		# Read csv as python dictionary
		reader = csv.DictReader(movie_csv)
		
		for row in reader:
			# Create media.Movie instances for each row
			# The arguments are: title, poster_image_url, introduction, stars, trailer_youtube_url
			movie_obj = media.Movie(
				row['title'], 
				row['image'], 
				row['introduction'],
				row['year'],
				row['type'],
				row['trailer_url']
			)
			# Store object in the list
			movie_list.append(movie_obj)

	return movie_list

# create a movie array
myMovies = get_movie_list('myMovies.csv')

# open the movie website page
fresh_tomatoes.open_movies_page(myMovies)
