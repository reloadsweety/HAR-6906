from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Todo(models.Model):
    todo_name = models.CharField(max_length=200)
    create_date = models.DateField('date publiched')
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name + "-" + str(self.is_check)
