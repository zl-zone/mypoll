# polls/models.py

from django.db import models

# 모델클래스
# 1. django.db.models.Model 상속
# 2. class 변수로 테이블의 컬럼과 연결된 변수(Model Field)를 선언.
#     - 변수명(컬럼명) = ModelField(type, 컬럼 제약조건 등)를 대입

# 질문(Question) 모델 - DB의 QUESTION 테이블과 연결.
class Question(models.Model):
    # 클래스 변수
    #   변수명: 컬럼명,
    #   Model Field 객체 - 컬럼 타입, 제약조건 설정.
    # primary key Field를 지정하지 않으면 id: 정수 자동증가 컬럼을 primary key 컬럼으로 생성
    question_text = models.CharField(max_length=200) # 문자열 타입. varchar(200)
    pub_date = models.DateTimeField(auto_now_add=True)   # 날짜/시간 타입
    # auto_add_now=True -> insert할 때 날짜/시간을 입력.
    
    def __str__(self):
        return f"{self.id}. {self.question_text}"


#  보기(Choice) 모델 - DB의 CHOICE 테이블과 연결

class Choice(models.Model):

    choice_text = models.CharField(max_length=200) # 보기문장
    votes = models.IntegerField(default=0) # 몇명이 선택했지 저장. 정수형.
    # Foreign key - QUESTION.id(PK) 참조
    question =  models.ForeignKey(
        Question, # 참조할 model클래스
        on_delete=models.CASCADE,  # 부모테이블의 참조값이 삭제된 경우 어떻게 할지.\
        # related_name="my_choice_set"        
    )
    
    def __str__(self):
        return f"{self.id}. {self.choice_text}"

