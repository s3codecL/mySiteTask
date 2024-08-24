from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Welcome to Django! My Site Task'
    username = 's3codecL'
    return render(request, 'index.html', {
        'title': title,
        'username': username
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
    username = 's3codecL'
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'project/projects.html', {
        'projects': projects,
        'username': username
    })

def tasks(request):
    username = 's3codecL'
    #task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {
        'tasks': tasks,
        'username': username
    })

def create_task(request):
    username = 's3codecL'
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {
            'form': CreateNewTask(),
            'username': username
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    username = 's3codecL'
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
            'form': CreateNewProject(),
            'username': username
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('create_project')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project/detail.html', {
        'project': project,
        'tasks': tasks
    })

def footer(request):
    username = 's3codecL'
    return render(request, 'layouts/footer.html', {
        'username': username
    })
