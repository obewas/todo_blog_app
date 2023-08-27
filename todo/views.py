from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView
from .models import Task
# Create your views here.

class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'task'
    fields = ('taskName', 'description', 'is_done')
    template_name = 'todo/task_create.html'
    success_url = '/'

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    fields = ('taskName', 'description', 'is_done')
    template_name = 'todo/task_update.html'
    success_url = '/'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/'

