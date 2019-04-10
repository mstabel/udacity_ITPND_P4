import webbrowser


class Movie(object):

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        '''
        inititalize a new instance of the class movie and sets the
        attributes: title, storyline, poster_image_url, trailer_youtube_url
        input:
        movie title, movie storyline, poster image url, youtube trailer url
        Returns: None
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url =trailer_youtube

    def show_trailer(self):
        '''
        instance method of the class movie, which opens the youtube trailer
        of the object in the webbroser
        Returns: None
        '''
        webbrowser.open(self.trailer_youtube_url)
