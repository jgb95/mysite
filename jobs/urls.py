from django.conf.urls import url, include
from jobs import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
    url(r'^postnewjob/$', views.post_new_job, name='postnewjob'),
    url(r'^postnewjob/thanks/(?P<id>\d+)/$', views.thanks, name='thanks')
]
