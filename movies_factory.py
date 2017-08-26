import json
import media

#reading JSON file and generating movies , which is list of Movie objects

#generate_from_json() is a static function which returns list of movie
def generate_from_json():
     
    #reading json data from "movies_json_data.json " file
    json_data=json.load(open("movies_data.json"))
    movies=[]
    #creating Movie object from Json Data making list of movie objects
    for i in json_data.keys():
        movie=media.Movie(json_data[i]["name"],json_data[i]["storyline"],json_data[i]["poster"],json_data[i]["trailer"])
        movies.append(movie)
    #returning list of movie
    return movies

