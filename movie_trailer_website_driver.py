import media
import fresh_tomatoes
import movies_factory


#Calling generate_from_json from movies_factory module 
movies=movies_factory.generate_from_json()

#passing list with movie objects to display trailers and posters
fresh_tomatoes.open_movies_page(movies)