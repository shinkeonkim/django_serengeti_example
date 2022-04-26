from django.urls import path
from .views import show

app_name = "article"

urlpatterns = [
    path('<int:id>', show, name="show"),
]
