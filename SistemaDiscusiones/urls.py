from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.home.urls', namespace="home")),
    url(r'^', include('apps.users.urls', namespace="users")),

    # PYTHON SOCIAL AUTH
    url('', include('social.apps.django_app.urls', namespace="social")),

    url(r'^admin/', include(admin.site.urls)),
)
