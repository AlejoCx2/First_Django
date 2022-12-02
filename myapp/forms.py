from cProfile import label
from pydoc import describe
from turtle import title
from django import forms

class createNewTask(forms.Form):

    title = forms.CharField(label="Titulo de la tarea", max_length= 200)
    dscription = forms.CharField(label="Descripcion", widget=forms.Textarea)


class createProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200)