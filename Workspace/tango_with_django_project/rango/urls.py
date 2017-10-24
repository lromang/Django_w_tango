from django.conf.urls import url
from rango import views

## Url Patterns
urlpatterns = [
    url(r'^$', views.index, name = 'index')
]
