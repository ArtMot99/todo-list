from django.urls import path
from .views import TaskListView, task_complete, task_undo, TaskCreateView


app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("complete_task/<int:task_id>/", task_complete, name="complete-task"),
    path("undo_task/<int:task_id>/", task_undo, name="undo-task"),
]
