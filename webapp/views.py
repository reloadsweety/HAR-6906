from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
'''


def index(request):
    context = {'todo_lists': Todo.objects.all()}
    return render(request, 'pages/index.html', context)


@csrf_exempt
def add_todo(request):
    name = request.POST.get('todo_name')
    print("NAME : %s" % name)
    todo = Todo(todo_name=name, create_date=timezone.now())
    todo.save()
    return HttpResponse("success")
