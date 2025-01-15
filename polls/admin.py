# polls/admin.py

from django.contrib import admin
from .models import Question, Choice
# .models -> 상대 경로로 import. admin.py와 같은 패키지에 있는 models.py
# admin app 에서 데이터를 관리할 수있도록 등록

admin.site.register(Question)
admin.site.register(Choice)


