
# My Site Task
![My Site Task Logo](./logo_mysite_task.png)

![GitHub contributors](https://img.shields.io/github/contributors/yourusername/yourrepository)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/yourrepository)
![GitHub issues](https://img.shields.io/github/issues/yourusername/yourrepository)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/yourrepository)
![GitHub forks](https://img.shields.io/github/forks/yourusername/yourrepository?style=social)
![PyCharm](https://img.shields.io/badge/pycharm-143?&logo=pycharm&logoColor=black&color=black&labelColor=green)

![Linux](https://img.shields.io/badge/Linux-FCC624?&logo=linux&logoColor=black)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?&logo=windows&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?&logo=bootstrap&logoColor=white)



## Introducción
My Site Task es una aplicación web desarrollada con Django para facilitar la gestión de tareas y proyectos. La aplicación permite a los usuarios crear, modificar, visualizar y eliminar proyectos y tareas, ofreciendo una interfaz intuitiva basada en Bootstrap para una experiencia de usuario fluida.

La aplicación está construida utilizando Django para el backend y sigue el patrón de diseño Modelo-Vista-Controlador (MVC). Gracias a su arquitectura escalable y su facilidad de configuración, My Site Task es ideal para equipos que necesitan una herramienta robusta para la gestión de proyectos y tareas.


## Stack Tecnológico
- ![Django](https://img.shields.io/badge/Django-092E20?&logo=django&logoColor=white)
- ![Python](https://img.shields.io/badge/Python-3776AB?&logo=python&logoColor=white)
- ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?&logo=bootstrap&logoColor=white)

## Sistemas Operativos Soportados
- ![Linux](https://img.shields.io/badge/Linux-FCC624?&logo=linux&logoColor=black)
- ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?&logo=ubuntu&logoColor=white)
- ![Windows](https://img.shields.io/badge/Windows-0078D6?&logo=windows&logoColor=white)

## Pruebas
Utilizamos `unittest` para las pruebas unitarias.

## Requerimientos

### Entidades / Funciones Clave de la Aplicación

#### Entidades:
- **Proyecto:**
  - `id`
  - `nombre`

- **Tarea:**
  - `id`
  - `título`
  - `descripción`
  - `estado` (completada o no)
  - `proyecto_id`

#### Funcionalidades:
- CRUD básico para proyectos y tareas.
- Listar todas las tareas de un proyecto.
- Marcar tareas como completadas.
- Eliminar tareas y proyectos.

## Cronograma de Desarrollo

- **CRUD básico:** 2 semanas
- **UI con Bootstrap:** 1 semana
- **Integración con base de datos:** 1 semana
- **Pruebas unitarias:** 1 semana

### Total estimado: 5 semanas

## Comunicación y Documentación

- **Slack:** Comunicación interna.
- **Notion:** Gestión de tareas y documentación del proyecto.
- **GitHub:** Control de versiones y colaboración en código.

## Clonar y Configurar el Proyecto

Para clonar y ejecutar este proyecto, necesitarás Git, Python y Django instalados en tu máquina. Desde tu terminal:

```bash
# Clonar este repositorio
git clone https://github.com/s3codecL/mySite

# Ir al directorio del repositorio
cd MySite

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
source ./venv/Scripts/activate  # En Windows
source ./venv/bin/activate      # En Linux/Mac

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
mv core/.env.example core/.env
nano core/.env  # Editar el archivo con los valores correspondientes

# Aplicar migraciones a la base de datos
python manage.py makemigrations
python manage.py migrate

# Crear un superusuario para acceder al administrador de Django
python manage.py createsuperuser
```

## Ejecución del Proyecto

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/admin/` y usa las credenciales del superusuario que creaste.

## Comandos Adicionales

Para crear una nueva aplicación en Django:

```bash
python manage.py startapp nombre_app
```

Recuerda añadir la nueva app al archivo `settings.py` en `INSTALLED_APPS`.


# Documentación técnica
![Django](https://img.shields.io/badge/Django-092E20?&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?&logo=bootstrap&logoColor=white)

## 1. Análisis del Código

El proyecto es una aplicación web desarrollada con Django que permite a los usuarios crear y gestionar tareas y proyectos. Utiliza Bootstrap para el diseño y la interfaz de usuario. El código sigue un patrón Modelo-Vista-Controlador (MVC), donde Django maneja la capa de control y acceso a datos, y Bootstrap se encarga del front-end.

### Eficiencia y Mejora
- **Modularidad:** El código está bien estructurado con una separación clara entre modelos, vistas y formularios, lo que facilita el mantenimiento y la escalabilidad.
- **Seguridad:** Es importante agregar validaciones adicionales en los formularios y asegurar que todas las entradas del usuario se manejen de manera segura para prevenir vulnerabilidades como inyecciones de SQL y XSS.
- **Escalabilidad:** Aunque el proyecto es pequeño, se recomienda considerar el uso de paginación en listas de tareas grandes y la optimización de consultas a la base de datos.

## 2. Explicación del Código

El código proporciona funcionalidades para:

- **Crear y gestionar proyectos:** Los usuarios pueden crear nuevos proyectos y asignarles un nombre.
- **Crear y gestionar tareas dentro de los proyectos:** Cada proyecto puede contener múltiples tareas, que pueden ser creadas, editadas o eliminadas.
- **Marcar tareas como completadas:** Los usuarios pueden marcar una tarea como completada, lo que actualiza su estado en la base de datos.
- **Eliminar tareas:** Las tareas pueden ser eliminadas permanentemente.

## 3. Modelado de la Base de Datos

### Estructura de la Base de Datos

La base de datos contiene dos modelos principales: `Project` y `Task`.

- **Modelo `Project`:**
    - `name`: Nombre del proyecto. Es un campo de texto con un máximo de 200 caracteres.

- **Modelo `Task`:**
    - `title`: Título de la tarea. Es un campo de texto con un máximo de 200 caracteres.
    - `description`: Descripción de la tarea. Es un campo de texto largo.
    - `done`: Estado de la tarea (completada o no). Es un campo booleano que por defecto es `False`.
    - `project`: Relación con el modelo `Project`. Es una clave foránea que indica a qué proyecto pertenece la tarea.

### Migraciones

Para aplicar los cambios en la base de datos, se utilizan las siguientes instrucciones:
```
python manage.py makemigrations
python manage.py migrate
```

### Detalle de los Modelos

#### Modelo Project:

```python
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```

#### Modelo Task:

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

## 4. Documentación Técnica

### Configuración del Proyecto

1. **Instalar dependencias:**
   ```
   pip install django
   ```

2. **Crear el proyecto Django:**
   ```
   django-admin startproject mysite
   cd mysite
   ```

3. **Crear la aplicación:**
   ```
   python manage.py startapp myapp
   ```

4. **Configurar `settings.py`:**
   ```python
   INSTALLED_APPS = [
       ...
       'myapp',
   ]

   TEMPLATES = [
       {
           ...
           'DIRS': [BASE_DIR / 'templates'],
           ...
       },
   ]
   ```

5. **Configurar `urls.py`:**
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),
   ]
   ```

### Modelos y Estructura de la Base de Datos

#### Relación entre los Modelos

- **Relación Project - Task:** Un proyecto puede tener múltiples tareas (`ForeignKey` en `Task`).
- **Creación de Tareas y Proyectos:** Se utilizan formularios en `forms.py` para crear nuevas tareas y proyectos.

#### Formularios

##### Formulario `CreateNewTask`:

```python
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
```

##### Formulario `CreateNewProject`:

```python
from django import forms

class CreateNewProject(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
```

### Interacción entre Modelos

#### Vistas

- **Vista `tasks`:** Muestra todas las tareas.
  
```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {'tasks': tasks})
```

- **Vista `delete_task`:** Elimina una tarea específica.
  
```python
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')
```

- **Vista `mark_done`:** Marca una tarea como completada.
  
```python
def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return redirect('tasks')
```

#### Configuración de URLs

```python
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('tasks/done/<int:task_id>/', views.mark_done, name='mark_done'),
]
```

### Consideraciones de Desarrollo

- **Pagos:** Añadir paginación a las vistas que manejan grandes cantidades de datos.
- **Autenticación:** Considerar agregar autenticación y permisos para gestionar acceso a proyectos y tareas.
- **Optimización:** Evaluar la optimización de consultas de base de datos utilizando `select_related` o `prefetch_related`.

### Pruebas Unitarias

- **Pruebas de Modelo:** Crear pruebas para validar la lógica de negocio en los modelos.
- **Pruebas de Vista:** Asegurar que las vistas manejen correctamente las peticiones y respuestas.

```python
from django.test import TestCase
from .models import Project, Task

class ProjectModelTest(TestCase):
    def test_project_creation(self):
        project = Project.objects.create(name="Test Project")
        self.assertEqual(str(project), project.name)

class TaskModelTest(TestCase):
    def test_task_creation(self):
        project = Project.objects.create(name="Test Project")
        task = Task.objects.create(title="Test Task", description="Test Description", project=project)
        self.assertEqual(str(task), task.title)
```

## 5. Estructura del Proyecto

```plaintext
mysite/
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── about.html
│   │   ├── index.html
│   │   └── task/
│   │       └── task.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── mysite/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

### Ejecución del Proyecto

1. **Iniciar el servidor de desarrollo:**
   ```
   python manage.py runserver
   ```
2. **Acceder a la aplicación:** 
   Abrir el navegador y navegar a `http://127.0.0.1:8000/`.
