from django.conf.urls import url, include

from . import views

app_name = 'registration'
urlpatterns = [
    url(r'^accounts/signup/$', views.register_user, name='sign_up'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
