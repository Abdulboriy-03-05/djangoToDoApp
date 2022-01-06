from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoAddForm
from django.views.generic.edit import UpdateView
from django.db.models import Q
# Create your views here.
def indexView(request):
    todos = Todo.objects.filter(done=False)
    doned_todos = Todo.objects.filter(done=True)
    return render(request, "index.html", {"tasks":todos, "doned_todos":doned_todos})

def doneTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = True
    todo.save()
    if todo:
        return redirect("/")
    return render(request, 'index.html')

def createTodo(request):
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TodoAddForm()
    return render(request, "todo.html", {"form":form})

def deleteTodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("/")

def deleteAllDonedTodos(request):
    doned_todos = Todo.objects.filter(done=True)
    doned_todos.delete()
    return redirect("/")

class UpdateTodoView(UpdateView):
    model = Todo
    fields = ['title', 'text', 'priority']
    template_name = 'todo.html'
    success_url = '/'

import json
def search(request):
    d = json.loads(request.GET["data"])
    print(d)
    obj = list(Todo.objects.filter(
    Q(title__icontains=d) | Q(text__icontains=d)).values())
    data = {}
    data["data"] = obj
    return JsonResponse(data)
