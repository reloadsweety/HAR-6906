from django.conf.urls import url

from . import views

app_name = "webapp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addtodo/$', views.add_todo, name='addtodo'),
]
