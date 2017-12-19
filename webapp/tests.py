from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Todo


class TodoModelTest(TestCase):
    def test_save_model(self):
        '''
            test create and save model to db
        '''
        todo_test1 = Todo(todo_name="test1", create_date=timezone.now())
        todo_test2 = Todo(todo_name="test2", create_date=timezone.now())
        todo_test1.save()
        todo_test2.save()
        todo_lists = Todo.objects.all().order_by("-create_date")
        self.assertQuerysetEqual(todo_lists, ['<Todo: test1>', '<Todo: test2>'])

    def test_remove_model(self):
        '''
            test create and delete model with todo_name
        '''
        todo_test1 = Todo(todo_name="test1", create_date=timezone.now())
        todo_test1.save()
        todo_lists = Todo.objects.all().order_by("-create_date")
        obj = Todo.objects.get(todo_name="test1")
        obj.delete()
        self.assertQuerysetEqual(todo_lists, [])


def create_simple_list():
    todo_test1 = Todo(id=50, todo_name="test1", create_date=timezone.now())
    todo_test2 = Todo(id=51, todo_name="test2", create_date=timezone.now())
    todo_test1.save()
    todo_test2.save()


class IndexViewTest(TestCase):
    def test_indexpage_is_avaliable(self):
        response = self.client.get(reverse("webapp:index"))
        self.assertEqual(response.status_code, 200)

    def test_indexpage_is_avaliable_and_show_tdodolists(self):
        create_simple_list()
        response = self.client.get(reverse("webapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['todo_lists'],
            ['<Todo: test1>', '<Todo: test2>']
        )

    def test_indexpage_when_add_todo_without_error_message_then_add_todo_and_redirect_to_indexpage(self):
        '''
        when post with url webapp:addtodo with todo_name if not have error_message then redirect to indexpage
        with status code 302 and then check todo_lists again
        '''
        create_simple_list()
        response = self.client.post(reverse("webapp:addtodo"), {'todo_name': 'test3'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("webapp:index"))

        response = self.client.get(reverse("webapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['todo_lists'],
            ['<Todo: test1>', '<Todo: test2>', '<Todo: test3>']
        )

    def test_indexpage_when_add_todo_with_blank_value_then_return_error_message(self):
        '''
        when post with url webapp:addtodo  with blank todo_name error_message
        then return error_message is 'can not add todo with blank value' and then render indexpage again
        '''
        create_simple_list()
        response = self.client.post(reverse("webapp:addtodo"), {'todo_name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error_message'], 'can not add todo with blank value')

    def test_indexpage_when_add_todo_with_duplicate_value_then_return_error_message(self):
        '''
        when post with url webapp:addtodo  with blank todo_name error_message
        then return error_message is 'todo is already exist' and then render indexpage again
        '''
        create_simple_list()
        response = self.client.post(reverse("webapp:addtodo"), {'todo_name': 'test1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error_message'], 'todo is already exist')

    def test_indexpage_when_remove_todo_then_remove_todo_and_redirect_to_indexpage(self):
        '''
        50 ,51 is todo.id for Test1 and Test2 form simple list
        when post with url webapp:removetodo then redirect to indexpage
        with status code 302 and then check todo_lists again
        '''
        create_simple_list()
        response = self.client.post(reverse("webapp:removetodo"), {'todos': [50, 51]})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("webapp:index"))

        response = self.client.get(reverse("webapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['todo_lists'], [])
