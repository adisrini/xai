from django.conf.urls import url

from . import views

app_name = 'explainable'
urlpatterns = [
    # /explainable/
    url(r'^$', views.index, name='index'),
    # /explainable/flip/
    # ...
    # /explainable/<module>/
    url(r'^example/$', views.example, name='example'),
    url(r'^(?P<route>[a-zA-Z]+)/$', views.module, name='module'),
]

# all pointing to same view (make sure to have optional default parameter for definition in view)
# urlpatterns = patterns('',
#     url(r'^project_config/$', views.foo),
#     url(r'^project_config/(?P<product>\w+)/$', views.foo),
#     ulr(r'^project_config/(?P<product>\w+)/(?P<project_id>\w+)/$', views.foo),
# )
