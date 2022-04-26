from django.urls import path
from .views import show, new

app_name = "article"

urlpatterns = [
    path('new', new, name="new"),
    path('<int:id>', show, name="show"),
]
