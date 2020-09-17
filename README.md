# :film_projector: 영화 추천 웹 사이트 구축 프로젝트 : GOD FILM :film_strip:

> 팀명 : 신세경
>
> 팀장 : 곽세경, 팀원 : 신현우



## 0. 배포 서버 

[:clapper: GOD FILM 바로가기](http://3.131.131.37/movies/)



## 1. 목표

- Django와 Vanila JS를 이용하여 영화 추천 웹 사이트를 구축한다.
- 커뮤니티 서비스를 구성하여 유저 간 소통을 가능하게 한다.
- API를 사용하여 data를 수집하고 다양한 서비스를 제공한다.
  - TMDB API, YOUTUBE API
- Django ORM을 사용하여 Data사용하고 영화 추천 알고리즘을 생성한다.





## 2. 사용 기술

- Python 3.7
- Django 2.1.15
- HTML5 + CSS3 + Bootstrap + Javascript

- 배포 
  - AWS + Nginx + uWSGI 



## 3. 역할 분담 및 개발 일정

<<<<<<< HEAD
![스크린샷 2020-09-01 오후 5.07.28](/Users/sekyung/Desktop/스크린샷 2020-09-01 오후 5.07.28.png)
=======
<img width="762" alt="역할분담" src="https://user-images.githubusercontent.com/60081217/93468750-6a903600-f92a-11ea-8efc-fbd65b2d2ff1.png">
>>>>>>> ff6df6adf0b1499334ade4cb8679fde6d5adc42e



#### 일정 관리는 노션 이용 

[:clapper:신세경팀 노션](https://www.notion.so/01e60c8029be4ddbada2ab620ee63ebe)



- 전체 일정 관리

<img width="772" alt="전체일정" src="https://user-images.githubusercontent.com/60081217/85582981-d55a0a00-b678-11ea-9b30-e0b08bd9c0f9.png">



- 세부 일정 정리

<img width="845" alt="일정1" src="https://user-images.githubusercontent.com/60081217/85582612-87450680-b678-11ea-9af0-ca6c72cee2b4.png">

<img width="1109" alt="일정2" src="https://user-images.githubusercontent.com/60081217/85582701-9af06d00-b678-11ea-9f72-30d544372c30.png">





## 4. ERD 모델링

<img width="1108" alt="ERD" src="https://user-images.githubusercontent.com/60081217/85584246-ef481c80-b679-11ea-8b58-a70446819faa.png">





## 5. 추천 알고리즘

- 영화 데이터와 배우 데이터를 이용하여 추천 알고리즘을 생성한다.
- loaddata가 가능하고, M:N관계가 가능하도록 형식에 맞추어 json 파일을 생성한다.

<img width="1076" alt="movie json" src="https://user-images.githubusercontent.com/60081217/85595282-a8f7bb00-b683-11ea-988c-f527bdafd57d.png">

- 영화 데이터의 json 파일

<img width="1044" alt="cast json" src="https://user-images.githubusercontent.com/60081217/85595273-a6956100-b683-11ea-9824-6430dc456ebf.png">

- **영화 데이터에 있는 배우 id로만 생성**된 cast.json 



#### 프로필 페이지의 추천 기능

<img width="664" alt="algo" src="https://user-images.githubusercontent.com/60081217/85595300-abf2ab80-b683-11ea-90d4-1df71280d21e.png">

- 사용자의 코멘트 데이터가 있는 경우, 없는 경우를 분기 시킨다.
- 데이터가 있는 경우에는 **점수를 기준으로 내림차순**을 한다.
- 없는 경우에는 **코멘트의 최신순에 따른 정렬**을 한다.

<img width="986" alt="html" src="https://user-images.githubusercontent.com/60081217/85595323-b0b75f80-b683-11ea-9eef-62c52f49fddd.png">

- **M:N 관계를 이용**하여 actor의 정보를 참조한다. 
- **포스터 정보가 없는 경우,** 사진이 깨지는 것을 방지하여 **분기를 시켜**주고 static폴더의 사진으로 대체시켜 준다.



#### 유투브 추천 기능

<img width="698" alt="api1" src="https://user-images.githubusercontent.com/60081217/85597723-d80f2c00-b685-11ea-857f-f413d5d5cc1d.png">

<img width="561" alt="api2" src="https://user-images.githubusercontent.com/60081217/85597713-d5acd200-b685-11ea-8ce7-2977e77edadd.png">

- 인증된 사용자, 인증되었지만 데이터가 없는 사용자, 인증되지 않는 사용자 셋을 분기하여 인풋값을 생성한다.

- params에 필수 인자값을 넣어 url과 함께 넘겨준다. 

  - **검색어와 관련된 q 태그에 인풋값을 연결**시켜준다.

- json형태로 받은 응답에서 필요한 value를 'items'키를 이용하여 접근한다.

  



## 6. 페이지 소개

#### 1. 첫 페이지

- 전체적인 디자인은 깔끔한 검정색에 핫핑크 색상으로 깔끔함과 통일감, 가독성있게 디자인 하였다.

- CSS의 마우스오버 속성을 사용하여, 메인 로고에 마우스를 가져다 올렸을 때 메뉴가 뜨게 한다.

- 인증된 사용자, 인증되지 않은 사용자를 분기하여 다른 메뉴를 안내한다.

<img width="1536" alt="인증놉" src="https://user-images.githubusercontent.com/60081217/85585409-f28fd800-b67a-11ea-98d2-3ca696580670.png">

- 인증되지 않은 사용자의 경우에는 **LOGIN, SIGNUP** 메뉴를 안내한다.

<img width="1536" alt="로그인" src="https://user-images.githubusercontent.com/60081217/85585247-cb390b00-b67a-11ea-9f44-ade7d17f0503.png">

- 인증된 사용자의 경우, **LOGOUT, MY PAGE** 를 안내한다.



#### 2. 영화 목록 페이지

- 추천하는 영화를 **Youtube API**를 이용하여 예고편을 현재 페이지에서 볼 수 있도록 구현하였다.
  - 인증된 사용자의 경우에는 **별점을 기반으로 최고점을 준 영화에 출연한 배우의 다른 영화를 추천**한다.
  - 사용자에 대한 데이터가 없는 경우 **최근 별점을 부여받은 영화를 추천**한다.

<img width="1536" alt="youtube" src="https://user-images.githubusercontent.com/60081217/85586818-333c2100-b67c-11ea-82de-ef19f2867f19.png">

- **TMDB API**를 사용하여 최신 영화에 대한 데이터를 117개 가져옴.
- **마우스 오버 속성을 이용**하여 마우스를 가져다 댈 때 에만 영화에 대한 상세 설명이 보이게 한다.
- **Pagination**을 통해 사용자가 편리하게 다양한 영화를 볼 수 있도록 구성함.

<img width="1536" alt="영화 리스트" src="https://user-images.githubusercontent.com/60081217/85587492-c8d7b080-b67c-11ea-816e-54886510e9c0.png">

#### 3. 영화 상세 페이지

- 영화 포스터와 영화 상세 설명을 확인할 수 있음.

<img width="1536" alt="디테일" src="https://user-images.githubusercontent.com/60081217/85589294-67184600-b67e-11ea-950b-b4021343f85c.png">

- **TMDB API**를 사용하여 배우에 대한 데이터를 612개 가져옴.

<img width="1536" alt="케릭터" src="https://user-images.githubusercontent.com/60081217/85589542-9c249880-b67e-11ea-82b6-07ae12315703.png">

- 해당 영화에 대해 리뷰 작성이 가능하며, 해당 영화에 대한 리뷰 확인이 가능하다.

- 별점과 함께 짧은 코멘트를 작성할 수 있으며, 다른 유저의 코멘트와 별점, 평점을 확인 할 수 있다.
  - 별점은 최소 1점 부터 최대 10점 까지 부여할 수 있다.
  - **본인이 쓴 코멘트는 삭제, 수정이 가능**하다.

<img width="1536" alt="리뷰" src="https://user-images.githubusercontent.com/60081217/85589765-cb3b0a00-b67e-11ea-9caa-a8395157dd7f.png">

#### 4. 리뷰 페이지

- Bootstrap의 Table 형식을 사용하여 구현
- **영화 이름, 리뷰 제목, 작성자 모두 클릭이 가능**하며 각 각 알맞은 페이지로 이동한다
  - 영화 이름을 선택할 시 영화의 상세페이지로 이동, 리뷰 제목을 선택할 시에는 리뷰 상세 페이지, 작성자를 선택할 때에는 작성자의 프로필 페이지로 이동한다.

<img width="1536" alt="리뷰 목록" src="https://user-images.githubusercontent.com/60081217/85591014-dfcbd200-b67f-11ea-86f3-30ea746ca909.png">

- 모든 리뷰에 **좋아요와 코멘트를 작성**할 수 있다.
- 리뷰 상세 페이지의 영화 제목을 클릭하면 영화의 상세 페이지, 작성자를 클릭하면 프로필 페이지로 이동한다.
- 리뷰 작성자는 **본인의 리뷰를 삭제, 수정 가능**하다.

<img width="1536" alt="리뷰 상세" src="https://user-images.githubusercontent.com/60081217/85591107-f83bec80-b67f-11ea-9aee-af36d2f22703.png">

#### 5. 프로필 페이지

- 팔로잉, 팔로우, 댓글, 리뷰, 좋아요 수를 확인할 수 있다.
- 본인의 프로필 페이지일 경우
  - 본인이 별점을 부여한 영화들 중에 **최고점을 받은 영화에 출연한 배우들의 다른 영화가 추천**된다.
  - 사용자의 별점 데이터가 없는 경우에는 **최근에 코멘트가 달린 영화에 출연한 배우들의 다른 배우가 추천**됨.

<img width="1536" alt="자신" src="https://user-images.githubusercontent.com/60081217/85592653-51f0e680-b681-11ea-9d50-780cfa7b8735.png">

- 프로필에서 **본인이 작성한 리뷰와 코멘트를 바로 삭제** 할 수 있다.
- 본인이 작성한 리뷰, 코멘트, 좋아요 한 게시글을 확인 할 수 있으며, **more 버튼을 통해 상세페이지로 바로 이동 가능**하다.

<img width="1536" alt="자신2" src="https://user-images.githubusercontent.com/60081217/85592672-54ebd700-b681-11ea-9f93-1c242d696328.png">

- 다른 유저의 프로필 페이지일 경우
  - 팔로우 버튼을 이용하여 **다른 유저를 팔로우** 할 수 있다.
  - 타인의 추천 영화는 보이지 않는다.

<img width="1536" alt="다른 사람" src="https://user-images.githubusercontent.com/60081217/85592553-3d145300-b681-11ea-85a6-5154c0a5d606.png">





## 7. 느낀점 및 오류 정리

- TMDB API를 활용하고 `requests`와 ` json`모듈을 사용하여  JSON 파일로 처리하고 `fixtures`를 사용하여 DB에 저장하였다.
  - `loaddata`로 모델에 더미데이터를 입히는 과정에서 많은 오류가 발생하였다.
  - 여러번 오류를 확인한 결과 `model`, `id`, `fields` 형태의 더미데이터만이 `loaddata`가 가능했다.
- **조건에 따른 분기를 설정**하지 않아 오류가 많이 발생했다.
  - 데이터가 없는 경우 youtube 의 input값이 존재하지 않는 다는 것을 여러번 오류를 발견한 후 수정할 수 있었다.
  - 항상 context를 통해 html에 일정값을 넘겨주게 되는데, 인증된 사용자, 인증은 했지만 데이터가 없는 경우, 인증되지 않는 경우를 전부 분기시키고 알맞은 값을 부여한 후 수월하게 작동되는 것을 확인할 수 있었다.

- **git에 api key를 올리게 될 때의 문제점**

  - github에 apikey를 그대로 올리게 되면 안내메일이 오게 된다. 구글 apikey를 그대로 노출하게 되면 범죄의 위험이 있기 때문에 반드시 숨겨서 올려야 한다.
  - youtube api, TMDB api를 사용하게 되면서 api key의 숨김 처리가 필요했다.
  - `secrets.json` 파일을 따로 만들고 settings에 for 문을 통해 변수로 `key` , `values` 를 이용하여 동적으로 기입

  <img width="575" alt="secrets" src="https://user-images.githubusercontent.com/60081217/85599798-d34b7780-b687-11ea-95e7-e17f7e455ed5.png">

  - 동적으로 기입한 후 `getattr` 을 이용하여 settings에 기입된 key 값을 불러와서 사용한다.

- **분업의 필요성**

  - 이번 프로젝트에서는 분업이 약간 실패했다. 서로 소통이 부족했고, 조급한 마음에 적당한 분업화가 이루어지지 않아서 각자의 역량을 완벽하게 드러내지 못한 점이 조금 아쉽게 느껴진다. 다음에는 많은 소통과 서로를 믿고 프로젝트를 진행해야 한다는 것을 느꼈다.

- **일정관리의 중요성**

  - 데드라인이 정해져 있는 프로젝트인 만큼 일정관리가 매우 필요하다고 느껴졌다. 
  - 처음에는 큰 틀을 잡고 프로젝트를 진행하면서 세부적인 일정을 잡게 되었다. 조금 빠듯한 감이 있었지만 확실히 일정을 정하고 난 후에 프로젝트를 진행하니 버려지는 시간이 적고 기간내에 차근차근 끝낼 수 있었다.
