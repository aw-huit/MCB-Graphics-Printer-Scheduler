from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mcb_printer_scheduler.views.home', name='home'),
    # url(r'^mcb_printer_scheduler/', include('mcb_printer_scheduler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^poster-printer/graphics-admin/', include(admin.site.urls)),
    
    url(r'^poster-printer/calendar/', include('mcb_printer_scheduler.schedule_viewer.urls')),

    url(r'^poster-printer/signup/', include('mcb_printer_scheduler.reservation_signup.urls')),

    url(r'^poster-printer/admin-signup/', include('mcb_printer_scheduler.admin_signup.urls')),

    #url(r'^poster-printer/user-auth/', include('mcb_printer_scheduler.login.urls')),

    url(r'^poster-printer/history/', include('mcb_printer_scheduler.reservation_history.urls')),

    url(r'^poster-printer/faqs/', include('mcb_printer_scheduler.faqs.urls')),
    
    #url(r'^poster-printer/hu-auth/', include('mcb_printer_scheduler.login.urls')),
    
    url(r'^poster-printer/hu-azp/', include('mcb_printer_scheduler.hu_authz_handler.urls')),
    
    url(r'^poster-printer/logos/', include('mcb_printer_scheduler.design_links.urls')),
    #url(r'^mcb/hu_auth/', include('mcb_printer_scheduler.login.urls')),

    (r'^poster-printer/media/(?P<path>.*)$', 'django.views.static.serve'\
        , {'document_root': settings.MEDIA_ROOT }),
    
    url(r'^poster-printer/$', include('mcb_printer_scheduler.schedule_viewer.urls')),
    
    #(r'^$', RedirectView.as_view(url='/poster-printer/calendar/')),
    
)

urlpatterns += staticfiles_urlpatterns()