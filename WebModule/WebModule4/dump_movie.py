import mlab
from models.movies import Movie
from models.users import User

mlab.connect()
for movie in Movie.objects():
    print(movie.title)
    print(movie.user.username)
    print("--------")

# Movie.drop_collection()