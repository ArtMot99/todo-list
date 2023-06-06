from django.urls import path
from .views import TaskListView


app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list")
]
