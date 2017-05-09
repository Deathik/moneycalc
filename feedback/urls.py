from django.conf.urls import url

from . import views

app_name="feedback"
urlpatterns = [
    url(r'form_handler/', views.feedback_form_handler, name='form_handler'),
]