from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from todo.forms import TaskForm
from todo.models import Tag


class TaskFormTests(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="test_tag")

    def test_valid_deadline(self) -> None:
        form_data = {
            "content": "Task 1",
            "deadline": timezone.now().date() + timedelta(days=1),
            "is_done": False,
            "tags": [self.tag],
        }
        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid(), form.errors)

    def test_past_deadline(self) -> None:
        form_data = {
            "content": "Task 2",
            "deadline": timezone.now().date() - timedelta(days=1),
            "is_done": True,
            "tags": [self.tag],
        }
        form = TaskForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn("deadline", form.errors)
        self.assertEqual(
            form.errors["deadline"][0], "The deadline cannot be in the past"
        )

    def test_missing_deadline(self) -> None:
        form_data = {
            "content": "Task 3",
            "is_done": False,
            "tags": [self.tag],
        }
        form = TaskForm(data=form_data)

        self.assertTrue(form.is_valid())
