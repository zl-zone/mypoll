1. 프로젝트 생성
mkdir   mypoll  - project 디렉토리
cd  mypoll
- project 생성:   `django-admin  startproject  config  .`
   config: 설정파일들을 저장하는 디렉토리.

- django-admin   startproject  test_project
   - test_project 라는 프로젝트를 직접 생성.

- 개발서버 실행.
   -  mypoll >  `python  manage.py  runserver`

2. App 생성
   1. mypoll> `python  manage.py  startapp  polls`
            - polls: app이름
   2. 생성한 app을 프로젝트에 등록
        - config/settings.py
            - INSTALLED_APP 에 polls 를 등록
        - settings.py에 추가 설정
            - LANGUAGE_CODE = 'ko-kr'
            - TIME_ZONE = 'Asia/Seoul'
        - config/urls.py
        - 파일생성 - polls/urls.py

3. 관리자(superuser) 계정 생성 (터미털 - control + `)
   - mypoll >  python  manage.py  migrate
   - mypoll >  python manage.py createsuperuser
      - 사용자 이름:  username (root)
      - email 주소:  a@a.com
      - Password: 1111
   - python manage.py runserver
      - http://127.0.0.1:8000/admin


4. Model 정의
   1. Model 클래스 정의 (polls/models.py)
   2. admin.py에 모델클래스 등록
   3. python manage.py makemigrations  app이름름
        - DB에 테이블을 생성/수정할 코드를 생성.
   4. python manage.py  migrate
        - DB에 테이블을 생성/수정 한다.
   - python manage.py runserver
      - http://127.0.0.1:8000/admin