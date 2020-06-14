import requests
import json



results = []
cast = []

for i in range(1, 10):
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=d689b32a04ce5d8848100e823ed584d7&language=ko-KR&page=" + str(i)
    data = requests.get(url).json()["results"]
 
    for i in data:
        new = {}
        new['model'] = 'movies.movie'
        movie_id = i.pop('id')
        new['id'] = movie_id
        
        url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/credits?api_key=d689b32a04ce5d8848100e823ed584d7"
        cast_data = requests.get(url).json()["cast"]
        cast_id = []
        # print(cast_data)
        cnt = 0
        for c in cast_data:
            cast_id.append(c["id"])
            cnt += 1
            if cnt == 5: break

        k = {}
        for key, value in i.items():
            if key in ['title', 'overview', 'vote_average', 'poster_path', 'like_users']:
                k[key] = value
            k['cast'] = cast_id

        print(k)
        new['fields'] = k
        results.append(new)


        # for data in results:
        #     data["fileds"][]

with open('movies.json', 'w', encoding="UTF-8") as make_file:
        json.dump(results, make_file, indent="\t") 