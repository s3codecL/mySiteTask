from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render

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
    return render(request, 'task.html')