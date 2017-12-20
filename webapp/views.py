from django.views import generic, View
from .models import Todo
from django.utils import timezone
from django.shortcuts import redirect, reverse, render
'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))

    def index(request):
    context = {'todo_lists': Todo.objects.all()}
    return render(request, 'pages/index.html', context) reverse("webapp:index")
'''


class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'todo_lists'

    def get_queryset(self):
        return Todo.objects.all().order_by("-create_date")


class AddTodo(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get('todo_name')
        todo = Todo(todo_name=name, create_date=timezone.now())
        context = {'error_message': '', 'todo_lists': Todo.objects.all()}
        try:
            todo.save()
        except Exception as e:
            if 'unique constraint' in str(e):
                context['error_message'] = 'todo is already exist'
        '''
            context['error_message'] = 'can not add todo with blank value'
        '''
        if context['error_message']:
            return render(request, 'pages/index.html', context)
        return redirect(reverse("webapp:index"))


class RemoveTodo(View):
    def post(self, request, *args, **kwargs):
        todos = self.request.POST.getlist('todos')
        for id in todos:
            obj = Todo.objects.get(pk=id)
            obj.delete()
        return redirect(reverse("webapp:index"))
