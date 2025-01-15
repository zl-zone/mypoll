# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import forms

## 확장 User 모델 
# - AbstractUser로 구현: 기본 User(username, password)에 필드들을 추가하는 방식
# - AbstractUser 상속. 필드들 정의(username, password빼고 정의)
class User(AbstractUser):
    
    # Field들 정의 - table컬럼
    name = models.CharField(
        verbose_name="이름", # Form관련설정(label) - Form을 ModelForm을 만들 경우 form관련설정을 Model에 한다.
        max_length=50 # varchar(50)
    )
    email = models.EmailField(verbose_name="Email", max_length=100)
    # EmailField: varchar(100) -> 값이 이메일 형식인지(@ 가 있는지)를 검증.
    birthday = models.DateField(
        verbose_name="생일",
        null=True, # Null허용 (default: False - Not Null)
        blank=True # Form - 필수가 아니다.(default: False - required)
    )
    
    
    def __str__(self):
        return f"username: {self.username}, name: {self.name}"

