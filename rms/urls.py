from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns
from rms import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imgs/(?P<model>[a-z_\-]+)/(?P<pk>[0-9]+/?)/?$', views.ImgTemplateView.as_view()),
)

urlpatterns += opatterns
