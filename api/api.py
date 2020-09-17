
import requests
import json



results = []
cast = []
movielst = []

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

        # print(k)
        new['fields'] = k
        results.append(new)


with open('movies.json', 'w', encoding="UTF-8") as make_file:
        json.dump(results, make_file, indent="\t") 

for data in results:
    cast_list = data["fields"]["cast"]
    for cast_id in cast_list:
        person_url = "https://api.themoviedb.org/3/person/"+ str(cast_id) +"?api_key=d689b32a04ce5d8848100e823ed584d7&language=ko-KR"
        url = "https://api.themoviedb.org/3/person/" + str(cast_id) + "/movie_credits?api_key=d689b32a04ce5d8848100e823ed584d7&language=ko-KR"
        cast_data = requests.get(person_url).json()
        new = {}
        new['model'] = 'movies.cast'
        new['id'] = cast_id 
        k = {}
        

        movielist = []
        cast_movie = requests.get(url).json()["cast"]
        cnt = 0
        for movie in cast_movie:
            mv = {}
            for key, value in movie.items():
                if key == 'id':
                    movielist.append(value)
                    mv['model'] = 'movies.movielist'
                    mv['id'] = value
                hh = {}
                if key in ['original_title', 'poster_path']:
                    hh[key] = value

            mv['fields'] = hh
            movielst.append(mv)
            

            # for key, value in movie.items():
            #     if key in ['character', 'title', 'poster_path', 'overview']:
            #         m[key] = value
            # movie_list.append(m)
            cnt += 1
            if cnt == 5: break
        

        # for num in movielist:
        #     mv = {}
           
        #     kk = {}
        #     for movie in cast_movie:
            


        for key, value in cast_data.items():
            if key in ['name', 'gender', 'profile_path']:
                k[key] = value
            k['movielist'] = movielist 

        new['fields'] = k
        cast.append(new)

with open('cast.json', 'w', encoding="UTF-8") as make_file:
        json.dump(cast, make_file, indent="\t") 


with open('movielist.json', 'w', encoding="UTF-8") as make_file:
        json.dump(movielst, make_file, indent="\t") 



        
        
            