from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path('data/(?P<Did>[a-zA-Z0-9]+)/(?P<pk1>[0-9]+[{.}][0-9]+)/(?P<pk2>[0-9]+[{.}][0-9]+)/(?P<pk3>[0-9]+[{.}][0-9]+)',views.data),
    path('',views.data1)
]