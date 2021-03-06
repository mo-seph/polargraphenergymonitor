from django.conf.urls import patterns, url

from polargraph import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

	 # ex: /polargraph/pipeline/5/update/
    url(r'^pipeline/(?P<pipelineID>\d+)/$', views.show_pipeline, name='show_pipeline'),
    url(r'^pipeline/create/?$', views.create_pipeline, name='create_pipeline'),
    url(r'^pipeline/(?P<pipelineID>\d+)/update/$', views.update, name='update'),
    url(r'^pipeline/?$', views.index, name='list_pipelines'),
    url(r'^endpoint_data/(?P<endpointID>\d+)/$', views.get_gcode, name='get_gcode'),
    url(r'^endpoint/(?P<endpointID>\d+)/$', views.show_endpoint, name='show_endpoint'),
)

