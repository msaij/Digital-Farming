from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.contacts,name='contacts'),
    re_path('(?P<offset>\d{0,4})/$',views.contact_detail),
    path('feedback',views.feedback)
]