from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from todo.models import Tag, Task


class ModelTests(TestCase):
    def test_tag_str(self) -> None:
        tag = Tag.objects.create(name="test_tag")

        self.assertEqual(str(tag), tag.name)

    def test_task_str(self) -> None:
        task = Task.objects.create(
            content="New Test Task",
            deadline=timezone.now().date() + timedelta(days=1),
            is_done=False,
        )

        self.assertEqual(str(task), task.content)
