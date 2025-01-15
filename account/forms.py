# account/forms.py
## Form/ModelForm 클래스들을 정의
##  - 입력 폼당 하나씩 생성. 보통 등록폼, 수정폼 두가지를 만든다.

# Form
# class MyForm(forms.Form)

# ModelForm
# class MyForm(forms.ModelForm)

from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,  # 사용자 등록/생성 폼
    UserChangeForm     # 사용자  정보 수정 폼. 둘다 ModelForm
)
from .models import User

# 사용자 가입(등록)시 사용할 Form을 구성 
#                  - UserCreationForm 상속(username, pwd1, pwd2) + 추가항목
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User  # User model의 field를 이용해서 form field를 구성
        # fields = "__all__" # 모델의 모든 field들을 사용해서 form field구성
        fields = ["username", "password1", "password2", 
                "name", "email", "birthday"] # form field로 구성할 것들들을 명시.
        # exclude = ["필드명"] # 지정한 필드명을 제외한 나머지 필드드로 form 필드 구성.
        # fields와 exclude는 같이 설정할 수 없다.
        
        # input type을 변경 -> Widget
        ### {"field이름":Widget객체}
        widgets = {
            "birthday":forms.DateInput(attrs={"type":"date"}), #<input type='date'>
            # "name":forms.PasswordInput()
        }
        
    # ModelForm에서 기본 검증을 처리
    ## name: required
    ## email: required, email형식 체크
    ## birthday: 날짜 형식 체크
    
    # 사용자 정의 검증 (Form을 만들경우에는 Form에 작성. )
    # - clean(), clean_검증필드명()
    ## name은 두 글자 이상 입력
    def clean_name(self):
        # self.cleaned_data: dict - 기본 검증을 통과한 요청파라미터들.
        name = self.cleaned_data['name']
        if len(name) < 2 :
            raise forms.ValidationError("이름은 2글자 이상 입력하세요.")
        return name # 리턴해주는 값이 View가 사용하는 값.
    
        