from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse

from .models import TodoItem

# Create your views here.
def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'pages/home.html', {'todos': todos})

# add_task
def add_task(request):
    todo = TodoItem(title=request.POST.get('title'))
    todo.save()
    todos = TodoItem.objects.all()
    return TemplateResponse(request, 'layout/todo_list.html', {'todos': todos})

# update_task
def update_task(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return HttpResponse(status=200)

# delete_task
def delete_task(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    todo.delete()
    todos = TodoItem.objects.all()
    return TemplateResponse(request, 'layout/todo_list.html', {'todos': todos})

def clean_empty_todo_items(request):
    todos = TodoItem.objects.all()
    todos.delete()
    # redirect to home page
    return redirect('home')
