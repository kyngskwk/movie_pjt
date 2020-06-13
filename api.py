import requests
import json



results = []

for i in range(1, 10):
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=d689b32a04ce5d8848100e823ed584d7&language=ko-KR&page=" + str(i)
    data = requests.get(url).json()["results"]
 
    for i in data:
        new = {}
        new['model'] = 'movies.movie'
        new['id'] = i.pop('id')

        k = {}
        for key, value in i.items():
            if key in ['title', 'overview', 'vote_average', 'poster_path', 'like_users']:
                k[key] = value
        new['fields'] = k
        results.append(new)

with open('movies.json', 'w', encoding="UTF-8") as make_file:
        json.dump(results, make_file, indent="\t") 