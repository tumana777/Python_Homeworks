# Import json module
import json

# Opening file
with open("movies.json") as json_file:
    # Getting python type data from json file
    deserialized_data = json.load(json_file)
    
    # Parsing data and creating lists
    new_crime_movies = [movie for elem in deserialized_data for movie in elem["results"] if "Crime" in movie["genres"] and movie["release_date"][:4] > "2000"]
    old_drama_movies = [movie for elem in deserialized_data for movie in elem["results"] if "Drama" in movie["genres"] and movie["release_date"][:4] < "2000"]
    new_century_movies = [movie for elem in deserialized_data for movie in elem["results"] if movie["release_date"][:4] == "2000"]
    
    # Changing genres 
    for movie in new_crime_movies:
        for i in range(len(movie["genres"])):
            if movie["genres"][i] == "Crime":
                movie["genres"][i] = "New_Crime"
                
    # Changing genres 
    for movie in old_drama_movies:
        for i in range(len(movie["genres"])):
            if movie["genres"][i] == "Drama":
                movie["genres"][i] = "Old_Drama"
                
    # Adding genre
    for movie in new_century_movies:
        movie["genres"].append("New_Century")
    
    # Concatenate movie lists
    parsed_movies = new_crime_movies + old_drama_movies + new_century_movies

# Writing data in the same json file
with open("movies.json", "w") as json_file:
    json.dump({"Data" : parsed_movies}, json_file, indent=4)