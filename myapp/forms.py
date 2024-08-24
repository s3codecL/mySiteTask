from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de tarea', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'form-control'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))