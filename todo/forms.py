from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "is_done",
            "tags",
        )
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            )
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline.date() < timezone.now().date():
            raise ValidationError("The deadline cannot be in the past")

        return deadline
