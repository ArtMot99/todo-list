from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from todo.forms import TaskForm
from todo.models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 7


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


def task_complete(request, task_id) -> HttpResponse:
    task = get_object_or_404(Task, id=task_id)
    task.is_done = True
    task.save()
    return redirect("todo:task-list")


def task_undo(request, task_id) -> HttpResponse:
    task = get_object_or_404(Task, id=task_id)
    task.is_done = False
    task.save()
    return redirect("todo:task-list")
