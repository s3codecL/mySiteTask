from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

# Create your views here.
def index(request):
    title = 'Welcome to Django!'
    return render(request, 'index.html', {
        'title': title
    })
def hello(request, username):
    print(type(username))
    return HttpResponse('<h1>Hello %s</h1>' % username)
def about(request):
    username = 's3codecL'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('/tasks/')

