from django.conf.urls import patterns, include, url
from illustrations import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'about/', views.about, name='about'),
        ]
