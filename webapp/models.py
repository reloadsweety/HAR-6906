from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Todo(models.Model):
    todo_name = models.CharField(max_length=200, unique=True)
    create_date = models.DateField('date publiched')

    def __str__(self):
        return self.todo_name
