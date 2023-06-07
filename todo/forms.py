from django import forms
from django.forms import DateTimeInput

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "is_done", "tags", )
        widgets = {
            "deadline": DateTimeInput(),
        }
