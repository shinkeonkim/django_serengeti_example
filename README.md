# Django 세렝게티 예제

- 기본적인 커뮤니티 사이트를 만들어봅니다.
- 기본적인 MTV 패턴에 대해서 다룹니다.
- CRUD 기능을 모두 활용해봅니다.
- AbstractBaseUser를 상속받은 유저의 회원가입/로그인을 다룹니다.
- Django Form을 활용해, 입력 폼을 구성합니다.

## 실습 순서

- django startproject  → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/4db9fbf1245878d77e5146b349b229bba98be2f0)
- 가상환경 만들기
- git init 
- .gitignore, README.md 등의 파일을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/c38d892be73f866d4b8e44273d32f6b8186f66f5)
- requirements.txt 파일을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/1db3f607f89bf6eed5c92163d7705ee72daa3b7b)
- main app을 생성합니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/f9b443874842447a0cad00a96894830d75721859)
  - root(/) 페이지를 임시로 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/0d911eaa325a5b77c87646049e3304ce5cc5f90d)
- user app을 생성합니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/bf2b8e3750ab7ff821df83a0176ab4ae43399a00)
  - AbstractBaseUser 상속한 User 모델을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/829142a3beb8e1ec46bbcdf726d442cca127a4ba)
  - 유저 회원가입 Form 클래스 (UserRegistrationForm)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/ff213811b84ecbc79451263c7f085c3ee1b0021a)
  - 유저 로그인 Form 클래스 (UserCreationForm)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/794b5e399e319bbc6d940468d49923f59c80ff94)
  - 회원가입 View와 Template (/users/signup)을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/5c936260eb309b0f90918b158b3a2555fa109370)
  - 로그인 View와 Template (/users/signin)을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/eac6e091f9367b102c23fa28b795e9c56fc3bbe1)
  - 로그아웃 View (/users/signout)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/faa7ea67eebb048602cc3f24ced0c03aca97fb63)
  - 회원가입, 로그인, 로그아웃 링크를 root 페이지에 연결합니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/94bc26389e36fd8caee6872e6ea557d82d370dea)
- article app을 생성합니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/8556a816d4bdb4a7c86f396e26fd2624f984182b)
  - Article 모델을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/579748d2378ad04c6297ad4cf3f9cef66d71abdb)
  - Article 생성/수정 Form 클래스 (ArticleForm)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/432294c4cde10d0db85ec14116bc2c9310445bb2)
  - Article 상세 View 와 Template (/articles/:id)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/6ece07a32d605f91ca0b11acef61cbd7eb304845)
  - Article 생성 View 와 Template (/articles/new)을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/6239ca3eb6811278690756e1535e11a8c1f57c36)
  - Article 수정 View 와 Template (/articles/:id/edit)을 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/e8b126a4c202b0617ddebde7b6cf6ac33d954be3)
  - Article 삭제 View (/articles/:id/destory)를 만들어봅니다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/6d5bd31e6d978bc188a2a4a3477b9c06fd708093)
  - Article 목록을 루트 페이지에서 나타나도록 해봅시다. → [관련 커밋 보기](https://github.com/shinkeonkim/django_serengeti_example/commit/b703addd3ab971a5344309b69a18c94b39768327)
- github에 올리기

## 과제

커뮤니티 사이트는 여러 기능들이 파생될 수 있습니다.

한번 직접 구현하면서, 아래 목록 중 1가지는 포함하여 만들어볼까요?

- 난이도 하 - 유저 프로필 페이지를 만들어봅시다.
- 닌이도 하 - 페이지네이션 기능을 통해 글이 한번에 보이지 않도록 해봅시다.
- 난이도 하 - 내가 작성한 글만 수정할 수 있도록 해봅시다.
- 난이도 하 - 사이트를 디자인해봅시다.
- 난이도 중 - 댓글 기능을 만들어봅시다.
- 난이도 중 - 좋아요 기능 / 북마크 기능을 만들어봅시다.
- 난이도 중 - 해쉬태그 기능을 만들어봅시다.
- 난이도 중 - 비밀번호 변경 기능을 만들어봅시다.
- 난이도 상 - 카카오톡/페이스북 로그인 기능을 만들어봅시다.
- 난이도 상 - 그룹 기능을 만들어봅시다.
- 난이도 상 - 회원가입 시, 메일을 보내 인증하는 기능을 만들어봅시다.
- 난이도 상 - 다른 사람도 사용할 수 있게 배포해봅시다.
