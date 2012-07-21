from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import assignment.assignment_urls
import assignment.syllabus_urls
import course.urls

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^logout/', 'front.views.logout_session'),
    (r'^$', 'front.views.welcome'),
    (r'^home/', 'front.views.index'),
    (r'^course/', include(course.urls)),
    (r'^assignment/', include(assignment.assignment_urls)),
    (r'^syllabus/', include(assignment.syllabus_urls)),
    (r'^library/catalog/', 'library.views.catalog'),
)
