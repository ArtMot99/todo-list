from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from todo.models import Task


class TaskListView(ListView):
    model = Task
    paginate_by = 7


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
