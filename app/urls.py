from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^summary$', views.summary),
    # url(r'^summary-average$', views.summary-avg),
    url(r'^sites$', views.home),
    url(r'^sites/first/$', views.first),
]