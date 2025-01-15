from django.urls import path
from . import views   # polls/views.py 모듈 import
app_name = "polls"

# 요청 url - 실행할 view 
## path("url", view함수, name="이 설정이름")
urlpatterns = [
    path("welcome", views.welcome, name="welcome"),
    path("vote_list", views.list, name="list"),
    path("vote_form/<int:question_id>", views.vote_form, name="vote_form"),
    path("vote", views.vote, name="vote"),
    path("vote_result/<int:question_id>", views.vote_result, name="vote_result"),
    path('vote_create', views.vote_create, name="vote_create"),
    path('', views.list, name="polls_home"),  # http://127.0.0.1:8000/polls/
]
# http://127.0.0.1:8000/polls/list

# http://127.0.0.1:8000/polls/vote_form/3
# path parameter 변수 설정. <타입:변수이름>
## 타입: 문자열로 넘어온 값을 어떤 타입으로 변환할 지 지정.
## 변수이름: view의 어떤 파라미터에 값을 넘길지 view함수 파라미터이름