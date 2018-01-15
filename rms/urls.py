from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns
from rms import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^imgs/(?P<model>[a-z_\-]+)/(?P<pk>[0-9]+/?)/?$',
        views.ImgTemplateView.as_view(),
    ),
    url(
        r'^change_user/(?P<user>[a-z_\-]+)/?$',
        views.ChangeUser.as_view(), name="change_user",
    ),
]

urlpatterns += opatterns
