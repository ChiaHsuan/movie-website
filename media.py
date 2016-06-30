
# This is the paraent class 
class Video():
	def __init__(self, title, poster_image_url, introduction):
		self.title = title
		self.poster_image_url = poster_image_url
		self.introduction = introduction

# This is the child class Movie, inheried from Vedio
class Movie(Video):
	def __init__(self, title, poster_image_url, introduction, year, film_type, trailer_youtube_url):
		Video.__init__(self, title, poster_image_url, introduction)
		self.trailer_youtube_url = trailer_youtube_url
		self.year = year
		self.film_type = film_type