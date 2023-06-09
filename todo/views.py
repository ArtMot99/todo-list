from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(ListView):
    model = Task
    paginate_by = 7


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")

    def get_object(self, queryset=None):
        task_id = self.kwargs.get("task_id")
        return get_object_or_404(Task, id=task_id)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")

    def get_object(self, queryset=None):
        task_id = self.kwargs.get("task_id")
        return get_object_or_404(Task, id=task_id)


class TagListView(ListView):
    model = Tag
    paginate_by = 7


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")

    def get_object(self, queryset=None):
        tag_id = self.kwargs.get("tag_id")
        return get_object_or_404(Tag, id=tag_id)


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")

    def get_object(self, queryset=None):
        tag_id = self.kwargs.get("tag_id")
        return get_object_or_404(Tag, id=tag_id)


class TaskStatusUpdateView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo:task-list")
