import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_url = movie_poster_url
		self.trailer_url = movie_trailer_url
	
	def show_trailer(self):
		webbrowser.open(self.trailer_url)
		