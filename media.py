import webbrowser

class Movie:
    # Movie  __init__ method to create Movie objects with name,storyline,poster,trailer
    def __init__(self,movie_name,movie_storyline,movie_poster,movie_trailer):
        self.name=movie_name
        self.storyline=movie_storyline
        self.poster=movie_poster
        self.trailer=movie_trailer
    # show_trailer helps to display trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)