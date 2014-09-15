from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import HomePageView
from .views import SignUpView
from .views import LoginView
from .views import LogOutView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'survivalguide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),	
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
)
