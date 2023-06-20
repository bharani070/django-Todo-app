from django.shortcuts import render
from todo.models import Task

def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-updated_At')
    completed_Tasks = Task.objects.filter(is_completed=True).order_by('-updated_At')
    context = {
        'tasks' : task,
        'completed_Tasks' : completed_Tasks
    }
    return render(request, 'home.html', context)