from django.urls import path
from .views import show, new, edit, destroy

app_name = "article"

urlpatterns = [
    path('new', new, name="new"),
    path('<int:id>/edit', edit, name="edit"),
    path('<int:id>', show, name="show"),
    path('<int:id>/destroy', destroy, name="destroy"),
]
