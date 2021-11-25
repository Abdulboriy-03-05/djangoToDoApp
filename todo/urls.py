from django.urls import path
from .import views
app_name = "todo"
urlpatterns = [
    path('', views.indexView, name="index"),
    path("create/", views.createTodo, name="create")
]