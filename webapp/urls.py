from django.conf.urls import url

from . import views

app_name = "webapp"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addtodo/$', views.add_todo, name='addtodo'),
    url(r'^removetodo/$', views.remove_todo, name='removetodo'),
]
