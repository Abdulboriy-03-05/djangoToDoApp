from django.urls import path
from .import views

app_name = "todo"
urlpatterns = [
    path('', views.indexView, name="index"),
    path("create/", views.createTodo, name="create"),
    path("delete/<int:todo_id>", views.deleteTodo, name="delete"),
    path("done/<int:todo_id>", views.doneTodo, name="done"),
    path("deleteAll/", views.deleteAllDonedTodos , name="deleteAllDonedTodos"),
    path("update/<pk>",views.UpdateTodoView.as_view(), name='update')
]