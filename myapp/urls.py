from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    path('hello/<str:username>', views.hello, name='hellotatata'), #<int:id>
    path('projects/', views.projects, name='projects'),
    #path('tasks/<int:id>', views.tasks)
    path('tasks/', views.tasks, name='tasks'),
    path('create/task/', views.createTask, name='create_task'),
    path('create/project/', views.createProjects, name='create_project'),
    path('detailProject/<int:id>', views.detailProject, name='detail_project')
    
]