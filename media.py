
# This is the paraent class 
class Video():
	def __init__(self, title, cover_image_url, introduction):
		self.title = title
		self.cover_image_url = cover_image_url
		self.introduction = introduction

# This is the child class Movie, inheried from Vedio
class Movie(Video):
	def __init__(self, title, cover_image_url, introduction, youtube_trailer_url):
		Video.__init__(self, title, cover_image_url, introduction)
		self.youtube_trailer_url = youtube_trailer_url