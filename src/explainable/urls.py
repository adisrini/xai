from django.conf.urls import url

from . import views

app_name = 'explainable'
urlpatterns = [
    # /explainable/
    url(r'^$', views.index, name='index'),
    # /explainable/flip/
    # ...
    # /explainable/<module>/
    url(r'^(?P<route>.*)/$', views.module, name='module'),
]
