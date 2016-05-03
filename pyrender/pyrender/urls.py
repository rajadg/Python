from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyrender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^code/showfile', 'pyrender.code.listing.showfile'),
    url(r'^code/listfile', 'pyrender.code.listing.listfile'),
    
    url(r'^working/counter', 'pyrender.test.workbench.counter'),
    url(r'^working/recorder', 'pyrender.test.workbench.recorder'),
    url(r'^admin/', include(admin.site.urls)),
)
