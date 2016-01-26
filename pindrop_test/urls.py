from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pindrop_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^results/(?P<area_code>.*)$', 'pindrop_test.main.app.results'),
    url(r'^results/', 'pindrop_test.main.app.results')
)
