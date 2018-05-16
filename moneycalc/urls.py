"""moneycalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from feedback.forms import FeedbackForm

urlpatterns = [
    url(r'^$', TemplateView.as_view(extra_context={"form": FeedbackForm()}, template_name="index.html"), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^calculator/', include('calculator.urls')),
    url(r'^', include('register.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^', include('social_django.urls', namespace='social')),
    # url(r'^api/', include('api_v1.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^debug/', include(debug_toolbar.urls)),]