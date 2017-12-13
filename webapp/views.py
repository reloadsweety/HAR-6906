from django.shortcuts import render


'''
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))
'''


def index(request):
    context = {'listnums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    return render(request, 'pages/index.html', context)
