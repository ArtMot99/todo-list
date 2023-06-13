from django.test import TestCase, Client
from django.urls import reverse
from todo.models import Task, Tag


class ViewTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.tag = Tag.objects.create(name="test_tag")
        self.task = Task.objects.create(
            content="Test Task",
            is_done=False,
        )

    def test_task_list_view(self) -> None:
        url = reverse("todo:task-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_list.html")
        self.assertContains(response, self.task.content)

    def test_task_create_view(self) -> None:
        url = reverse("todo:task-create")
        form_data = {
            "content": "New Task",
            "deadline": "2023-07-15",
            "is_done": True,
        }
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_update_view(self) -> None:
        url = reverse("todo:task-update", kwargs={"task_id": self.task.id})
        form_data = {
            "content": "Updated Task",
            "deadline": "2023-07-15",
            "is_done": True,
        }
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_form.html")

    def test_task_delete_view(self) -> None:
        url = reverse("todo:task-delete", kwargs={"task_id": self.task.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo:task-list"))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_tag_list_view(self) -> None:
        url = reverse("todo:tag-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/tag_list.html")
        self.assertContains(response, self.tag.name)

    def test_tag_create_view(self) -> None:
        url = reverse("todo:tag-create")
        form_data = {
            "name": "New Tag",
        }
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

    def test_tag_update_view(self) -> None:
        url = reverse("todo:tag-update", kwargs={"tag_id": self.tag.id})
        form_data = {
            "name": "Updated Tag",
        }
        response = self.client.post(url, data=form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, "Updated Tag")

    def test_tag_delete_view(self) -> None:
        url = reverse("todo:tag-delete", kwargs={"tag_id": self.tag.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo:tag-list"))
        self.assertFalse(Tag.objects.filter(id=self.tag.id).exists())

    def test_task_status_update_view_with_post_method(self) -> None:
        url = reverse("todo:task-status-update", kwargs={"task_id": self.task.id})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("todo:task-list"))

    def test_task_status_update_view_get_method_not_allowed(self):
        response = self.client.get(
            reverse("todo:task-status-update", kwargs={"task_id": self.task.id})
        )

        self.assertEqual(response.status_code, 405)
