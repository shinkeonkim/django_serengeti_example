from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# AbstractBaseUsers는 장고에서 기본적으로 제공하는 추상 User 모델입니다.
# 비밀번호와 관련된 기능을 제공합니다. (그 외의 기능은 모두 직접 구현해줘야 합니다.)

class UserManager(BaseUserManager):
    def _create_user(self, username, password, **kwargs):
        """create_user와 create_super_user의 겹치는 부분을 줄여주는 메서드"""
        user = self.model(
            username = username,
            **kwargs,
        )
        user.set_password(password)
        user.save()
    
    def create_user(self, username, password, **kwargs):
        """일반 유저 생성 메소드"""
        self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        """슈퍼 유저(superuser) 생성 메소드"""
        kwargs.setdefault("is_superuser", True) 
        # 슈퍼 유저를 생성하는 것이기 때문에, is_superuser를 True로 설정해 _create_user 메서드로 넘깁니다.
        self._create_user(username, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )  # 사용자명
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 유저 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 유저 레코드가 수정된 일자
    
    objects = UserManager()

    @property
    def is_staff(self):
        # is_staff -> 어드민 페이지에 접근을 할 수 있다.
        # is_superuser -> staff 중에서도 모든 권한을 가지고 있는 유저
        # 현재 is_staff와 is_superuser를 다르게 생각하지 않는 프로잭트기 때문에 다음과 같이 동일시하고 있음.
        return self.is_superuser
