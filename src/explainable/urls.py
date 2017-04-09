from django.conf.urls import url

from . import views

urlpatterns = [
    # /explainable/
    url(r'^$', views.index, name='index'),
    # /explainable/flip/
    # ...
    # /explainable/<other_modules>/
    url(r'^(?P<route>.*)/$', views.module, name='module'),
]
