from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from api_v1 import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'calculator', views.CalculatorViewSet)

schema_view = get_schema_view(title='MoneyCalc API')
#Docs configuration
API_TITLE = 'MoneyCalc API Docs'
API_DESCRIPTION = 'This is detalized documentation for MoneyCalc app'

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]