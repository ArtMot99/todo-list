from django.urls import path
from .views import (
    TaskListView,
    task_complete,
    task_undo,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:task_id>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:task_id>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("complete_task/<int:task_id>/", task_complete, name="complete-task"),
    path("undo_task/<int:task_id>/", task_undo, name="undo-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:tag_id>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:tag_id>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
