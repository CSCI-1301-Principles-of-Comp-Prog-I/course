# Movies DB access using lists.  This uses this library:
#    https://pypi.org/project/tmdbv3api/
#
import pickle

def get_movies():
    movies = []
    with open('movie_db.data', 'rb') as filehandle:
        # read the data as binary data stream
        movies = pickle.load(filehandle)
    return movies
