from django.conf.urls import url

from . import views

app_name = "webapp"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addtodo/$', views.AddTodo.as_view(), name='addtodo'),
    url(r'^removetodo/$', views.RemoveTodo.as_view(), name='removetodo'),
]
