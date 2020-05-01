from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.add, name='add'),
    url(r'^', views.show, name='show'),
]
