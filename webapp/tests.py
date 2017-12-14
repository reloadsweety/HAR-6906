from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Todo


class TodoModelTest(TestCase):
    def test_save_model(self):
        todo_test1 = Todo(todo_name="test1", create_date=timezone.now())
        todo_test2 = Todo(todo_name="test1", create_date=timezone.now())
        todo_test1.save()
        todo_test2.save()

        self.assertEqual(len(Todo.objects.all()), 2)


class IndexViewTest(TestCase):
    def test_indexpage_is_avaliable(self):
        respone = self.client.get(reverse("webapp:index"))
        self.assertEqual(respone.status_code, 200)
