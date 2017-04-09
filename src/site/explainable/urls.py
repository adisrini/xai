from django.conf.urls import url

from . import views

urlpatterns = [
    # /explainable/
    url(r'^$', views.index, name='index'),
    # /explainable/flip/
    url(r'^flip/$', views.flip, name='flip'),
]
