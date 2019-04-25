from django.conf.urls import url
from . import views

urlpatterns = [
    #/college/
    url(r'^$', views.index , name='index'),
    #college/567/
    url(r'^(?P<college_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<college_id>[0-9]+)/basicinfo/$',views.basicinfo,name='basicinfo'),
    url(r'^(?P<college_id>[0-9]+)/course/$',views.course,name='course'),
    url(r'^(?P<college_id>[0-9]+)/reviews/$',views.reviews,name='reviews'),
    url(r'^(?P<college_id>[0-9]+)/facilities/$',views.facilities,name='facilities'),
    url(r'^(?P<college_id>[0-9]+)/gallery/$',views.gallery,name='gallery'),
    url(r'^(?P<college_id>[0-9]+)/contact/$',views.contact,name='contact'),

]