from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
'''


def index(request):
    context = {'a': 'a'}
    return render(request, 'pages/index.html', context)
