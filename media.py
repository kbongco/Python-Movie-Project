import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#self is instance of the class that's created, so your_name
#Once parameters are in the function, it can initialize
#First thing that happens, init is being called
#Once everything is declared approporiately then everything will run
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
