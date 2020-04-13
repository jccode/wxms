

from django.conf.urls import url
from wxcommon import views


urlpatterns = [
    url(r'^access-token$', views.access_token, name='access_token'),
    url(r'^jsapi-ticket$', views.jsapi_ticket, name='jsapi-ticket'),
]
