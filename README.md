# Django 세렝게티 예제

- 기본적인 커뮤니티 사이트를 만들어봅니다.
- 기본적인 MTV 패턴에 대해서 다룹니다.
- CRUD 기능을 모두 활용해봅니다.
- AbstractBaseUser를 상속받은 유저의 회원가입/로그인을 다룹니다.
- Django Form을 활용해, 입력 폼을 구성합니다.

## 실습 순서

- django startproject
- 가상환경 만들기
- git init
- .gitignore, README.md 등의 파일을 만들어봅니다.
- requirements.txt 파일을 만들어봅니다.
- main app을 생성합니다.
  - root(/) 페이지를 임시로 만들어봅니다.
- user app을 생성합니다.
  - AbstractBaseUser 상속한 User 모델을 만들어봅니다.
  - 유저 회원가입 Form 클래스 (UserRegistrationForm)를 만들어봅니다.
  - 유저 로그인 Form 클래스 (UserCreationForm)를 만들어봅니다.
  - 회원가입 View와 Template (/users/signup)을 만들어봅니다.
  - 로그인 View와 Template (/users/signin)을 만들어봅니다.
  - 로그아웃 View (/users/signout)를 만들어봅니다.
  - 회원가입, 로그인, 로그아웃 링크를 root 페이지에 연결합니다.
- article app을 생성합니다.
  - Article 모델을 만들어봅니다.
  - Article 생성/수정 Form 클래스 (ArticleForm)를 만들어봅니다.
  - Article 상세 View 와 Template (/articles/:id)를 만들어봅니다.
  - Article 생성 View 와 Template (/articles/new)을 만들어봅니다.
  - Article 수정 View 와 Template (/articles/:id/new)을 만들어봅니다.
  - Article 삭제 View (/articles/:id/destory)를 만들어봅니다.
  - Article 목록을 루트 페이지에서 나타나도록 해봅시다.
- github에 올리기

## 과제

커뮤니티 사이트는 여러 기능들이 파생될 수 있습니다.

한번 직접 구현하면서, 아래 목록 중 1가지는 포함하여 만들어볼까요?

- 난이도 하 - 유저 프로필 페이지를 만들어봅시다.
- 닌이도 하 - 페이지네이션 기능을 통해 글이 한번에 보이지 않도록 해봅시다.
- 난이도 중 - 좋아요 기능 / 북마크 기능을 만들어봅시다.
- 난이도 중 - 해쉬태그 기능을 만들어봅시다.
- 난이도 중 - 비밀번호 변경 기능을 만들어봅시다.
- 난이도 상 - 카카오톡/페이스북 로그인 기능을 만들어봅시다.
- 난이도 상 - 그룹 기능을 만들어봅시다.
- 난이도 상 - 회원가입 시, 메일을 보내 인증하는 기능을 만들어봅시다.
- 난이도 상 - 다른 사람도 사용할 수 있게 배포해봅시다.
