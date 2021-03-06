from django.conf.urls import include, url
from django.contrib import admin
from heroku import Views

urlpatterns = [
    # Examples:
    # url(r'^$', 'heroku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', Views.goToLogin),
    url(r'^authenticateUser/', Views.authenticateUser),
    url(r'^createUser/', Views.createUser),
]
