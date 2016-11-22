from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libreriaweb.views.home', name='home'),
    # url(r'^libreriaweb/', include('libreriaweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #INDEX
    url(r'^' , include('apps.inicio.urls')),    
    #AUTORS
    url(r'^autor/' , include('apps.autor.urls')),
    #BOOKS
    url(r'^libros/' , include('apps.libros.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT, } ),
)

