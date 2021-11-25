from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoAddForm
# Create your views here.
def indexView(request):
    tasks = Todo.objects.all()
    return render(request, "index.html", {"tasks":tasks})

def createTodo(request):
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TodoAddForm()
    return render(request, "todo.html", {"form":form})