from turtle import title
from unicodedata import name
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import createNewTask, createProject

# Create your views here.


def index(req):
    title = '¡¡ Django Course !!'
    return render(req, 'index.html', {
        'title': title
    })


def hello(req, username='Invitado'):
    return HttpResponse(f'<h1>Hey, Hello {username}</h1>')


def about(req):
    return render(req, 'about.html')


def projects(req):
    projects = Project.objects.all()
    return render(req, 'projects.html', {
        'projects': projects
    })


""" def tasks(req,id):
    task = get_object_or_404(Task,id=id )
    return HttpResponse(f'<h3>Tasks: {task.title}</h3>') """


def tasks(req):
    ts = Task.objects.all()
    return render(req, 'tasks.html', {
        'tasks': ts
    })


def createTask(req):
    if req.method == 'GET':
        return render(req, 'createTask.html', {
            'form': createNewTask()
        })
    else:
        Task.objects.create(
            title=req.POST['title'], dscription=req.POST['dscription'], project_id=1)
        return redirect('tasks')


def createProjects(req):
    if req.method == 'GET':
        return render(req, 'createProject.html', {
            'form': createProject()
        })
    else:
        Project.objects.create(name=req.POST['name'])
        return redirect('projects')

def detailProject(req, id):
    #project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(req, 'detailProjects.html',{
        'project': project,
        'tasks':tasks
    })