from django.urls import path
from .views import signup, signin

app_name = "user"

urlpatterns = [
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
]
