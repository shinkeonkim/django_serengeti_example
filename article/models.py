from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE
    )  # 작성자
    title = models.TextField()  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 글 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 글 레코드가 수정된 일자
